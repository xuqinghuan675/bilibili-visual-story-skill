import unittest,tempfile,json,subprocess,sys
from pathlib import Path
from check_caption_bounds import outside_edges,inspect_svg,run,run_manifest
class BoundsTests(unittest.TestCase):
 def test_inside(self): self.assertEqual(outside_edges([2,3,5,6],[0,0,10,10]),[])
 def test_exact_edge(self): self.assertEqual(outside_edges([0,0,10,10],[0,0,10,10]),[])
 def test_all_edges(self): self.assertEqual(outside_edges([-1,-1,12,12],[0,0,10,10]),['left','top','right','bottom'])
 def test_nonfinite(self):
  for b in ([0,0,float('nan'),1],[True,0,1,1],[0,0,0,1]):
   with self.assertRaises(ValueError): outside_edges(b,[0,0,10,10])
 def fixture(self,text):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup);p=Path(self.tmp.name)/'a.svg';p.write_text(text);return str(p)
 def sample(self,text='长连续中文测试文本',safe=None):
  return {'id':'test','text':text,'lines':[text],'safe_rect':safe or [0,0,200,100],'svg':self.fixture('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="100"><text x="10" y="50" font-family="Noto Sans CJK SC" font-size="20">'+text+'</text></svg>')}
 def test_real_cjk_overflow(self): self.assertEqual(inspect_svg(self.sample(safe=[0,0,40,100]))['geometry_status'],'FAIL')
 def test_real_fitting(self): self.assertEqual(inspect_svg(self.sample('可读'))['geometry_status'],'PASS')
 def test_long_token_no_autosplit(self):
  r=inspect_svg(self.sample('123456789012345678901234567890',safe=[0,0,40,100]));self.assertEqual(r['geometry_status'],'FAIL');self.assertEqual(len(r['lines']),1)
 def test_text_preserved(self):
  s=self.sample();s['lines']=['改动'];
  with self.assertRaises(ValueError):inspect_svg(s)
 def test_ambiguous(self):
  s=self.sample('重复');p=Path(s['svg']);t=p.read_text();p.write_text(t.replace('</svg>',t[t.index('<text'):t.index('</text>')+7]+'</svg>'))
  with self.assertRaises(ValueError):inspect_svg(s)
 def test_active_rejected(self):
  s=self.sample();p=Path(s['svg']);p.write_text(p.read_text().replace('</svg>','<script/></svg>'))
  with self.assertRaises(ValueError):inspect_svg(s)
 def test_unknown_font(self):
  s=self.sample();p=Path(s['svg']);p.write_text(p.read_text().replace('Noto Sans CJK SC','MissingFont_1234'))
  with self.assertRaises(ValueError):inspect_svg(s)
 def test_empty_samples_unverified(self):
  r=run([]);self.assertEqual(r['counts'],{'PASS':0,'FAIL':0,'UNVERIFIED':1})
 def test_nonlist_samples_unverified(self):
  for value in (None,{},'bad',42):
   with self.subTest(value=value):self.assertEqual(run(value)['counts']['UNVERIFIED'],1)
 def test_nonobject_rows_unverified(self):
  r=run([None,[],42,'bad']);self.assertEqual(r['counts']['UNVERIFIED'],4);self.assertEqual(r['counts']['PASS'],0)
 def test_invalid_manifest_root(self):
  for value in ([],None,{}, {'samples':[]}):
   with self.subTest(value=value):self.assertEqual(run_manifest(value)['counts']['UNVERIFIED'],1)
 def test_malformed_row_fields(self):
  s=self.sample();s['svg']=123;self.assertEqual(run([s])['counts']['UNVERIFIED'],1)
 def test_cli_bad_input_nonzero_json(self):
  with tempfile.TemporaryDirectory() as tmp:
   manifest=Path(tmp)/'manifest.json';out=Path(tmp)/'result.json'
   for text in ('{"samples": []}', '{"samples": [null]}', '[]', '{broken'):
    with self.subTest(text=text):
     manifest.write_text(text)
     p=subprocess.run([sys.executable,str(Path(__file__).with_name('check_caption_bounds.py')),str(manifest),'--output',str(out)],capture_output=True,text=True)
     self.assertNotEqual(p.returncode,0);self.assertNotIn('Traceback',p.stderr)
     self.assertGreater(json.loads(out.read_text())['counts']['UNVERIFIED'],0)
if __name__=='__main__':unittest.main()

