# Rendering and actual QA

Choose the visual medium deliberately: a watercolor character style is not a default for spatial 3D explanation; kinetic typography is not a vehicle-modeling system. Select the fixed reference route and write its treatment before adapting a demo. A technical demo does not replace that visual direction. Use a fixed seed and pure render(t), positive duration, explicit resource readiness and shared event/text/model state. World labels share the same projection transform as objects.

Distinguish implementation evidence: a working CPU SVG renderer, a browser WebGL/PBR renderer and an offline Cycles material still are separate capabilities. Report the one actually tested. Static approval does not establish motion, readability or audio quality.

Traffic objects must remain recognizable at mobile size: body silhouette, windows, wheels, front/back and ground contact; roads need surface, edges, markings and plausible width. Do not replace vehicles with tiny light beads without a stated abstraction appropriate to the task. Depth is conveyed by visible planes, light/shadow, occlusion, projection and contact, not a material name or dark filter.

For vehicles, consistently use the rear axle or center as the path reference. Derive steering from wheelbase and curvature; derive wheel rotation from traveled distance; inspect speed/curvature transitions and camera rate. Zero sampled collisions does not establish natural motion or continuous-time safety. Non-vehicle topics need not obey vehicle dynamics.

Retain a near-plane clipping regression: clip crossing triangles before projection, interpolate relevant attributes and verify materials/normals. Do not hide a disappearing-road defect through camera changes or a single-frame patch.

Review separately: model invariants; actual text bounds and fully-visible read time; full decode; full-size and 360px frames; per-shot contact sheets; action strips; cut-adjacent frames; normal-speed viewing; independent comprehension; audio listening. Mark each pass/revise/not_checked with exact scope and evidence. Playback time advancing, sampled screenshots, unique frames and successful decoding cannot substitute for continuous viewing. Unheard audio stays unchecked. Correct defects then inspect the actual revised output, not merely changed code.

## Cache provenance after a patch

Key cache reuse by hashes of the actual renderer source/bundle, relevant configuration and input content, not filenames, modification times or the mere existence of a frame. After a source/configuration change, regenerate or otherwise establish the final per-frame render inputs before deciding which raster frames remain valid. Reuse only frames whose rendered input content and rasterization settings are unchanged; invalidate and rerender affected frames. If dependencies or provenance are uncertain, widen invalidation rather than assume an unaffected range.

After the last patch and final encode, decode the delivered file and compare every frame with its corresponding final source raster, checking sequence, count and timing. Use a documented compression-aware comparison for lossy encoding, not byte equality; inspect unexpected differences. Keep source/configuration/content hashes and the comparison scope with the build record. This detects stale exports, not comprehension, motion quality or rights compliance; those require their separate reviews.


## Final-output identity and promotion

The following are recommended checks, not a claim that a renderer already implements them. Include both source-content identity and effective rendering/encoding parameters in cache and output provenance. File size, modification time and a success message cannot establish that the delivered bytes belong to the intended revision. Retain a content hash of the validated output.

Encode to a temporary artifact, check the encoder exit status, and validate that artifact before promoting it to the final name. Check the rename or replacement result separately; encoder success does not imply promotion success. Reopen the final path and compare its content hash with the validated artifact, then check the delivered stream properties. A failed promotion must leave the new delivery unconfirmed rather than silently accepting an older same-size file.

## Transferable implementation contracts

These contracts summarize inspected upstream methods and observed pitfalls. Documentation is not implementation or a passing test. Track source reading, example viewing, module execution, regression testing and final-film review separately.

1. Deterministic time. Record source/resource hashes, seed, dimensions, frame rate, duration and scene/camera definitions. Await font/image readiness. Compute state(t), then camera/world transforms and projected labels. Compare the same time rendered repeatedly and in forward, reverse and shuffled order within the same environment; wall-clock or previous-frame residue must not change state. Cross-environment raster differences need separate explanation.
2. Visible mechanism. Derive model, labels and outcomes from shared state. Declare controlled variables and distinguish a didactic illustration from physical simulation. Never secretly remove an object or alter a rule to produce a desired result. Preserve identity during decomposition/reassembly. A director-controlled traffic animation is not proof of equilibrium or natural driving.
3. Continuity and reading. Separate camera motion, object motion and state change. Inspect cut-adjacent frames and normal-speed motion for orientation, occlusion, clipping, labels and endpoint speed. Begin reading-time measurement only after the complete text is stable; recalculate after replacement, re-entry or occlusion. Character-rate heuristics are screening tools, not comprehension or platform rules.
4. Encoded output. Reopen and fully decode the final file; verify frame order/count, resolution, timing, expected audio tracks and the start/end. Measure audio after encoding and listen separately. A short audio track must not silently truncate video. Target loudness values are project choices, not automatically platform requirements.
5. Failure handling. Capture renderer errors and encoder return codes/stderr. Isolate output jobs, use exclusive output ownership, and expose a final artifact only after validation. A success log, nonempty JPEG or existing file does not establish valid output. Test missing fonts, missing/corrupt frames, stale manifests, encoder failure and output-lock conflicts before claiming fail-closed behavior. Do not copy unsafe launch flags or destructive cleanup paths.
6. Bounded module trials. Test a representative short segment before estimating a full render budget, and record omitted shaders/objects, substituted materials, camera changes and known ordering defects. An upstream geometry/time module rendered through a CPU adaptation verifies that limited path only, not the original PBR, ambient occlusion, depth of field or whole film. Do not present upstream demonstrations as original educational films.

Specific inspected counterexamples: PDoomVideo's legacy time entry does not by itself replace runtime animation time; its clip export path and file-size resume checks require independent exit-status and content validation. Lemo's illustrative traffic choreography and wheel behavior require model-specific verification. These are revision-bound findings, not claims about every future upstream version. See [source identities and rights](attribution.md).


## Local geometry and comparison regressions

Testing a particle center inside a liquid region is insufficient when its visible corners or outline cross the changing surface. Test the rendered shape against the evolving boundary and floor, with a stated screen-space margin, over the affected time range. Use exact containment for the relevant geometry; corner-only checks do not prove containment for arbitrary curved shapes or non-convex regions. A close-up may use a separate illustrative particle set, but label that identity domain rather than pretending that it is the full scene's unchanged population.

Inspect the obstacle, contact line and moving particles at both full size and mobile width. Essential model conditions belong in stable main captions; secondary notes must not overlap object outlines. Independently inspect transitions into and out of comparison scenes and separate shape, composition and boundary-condition changes. Passing a local regression does not certify the entire film.

## Content-addressed revision example

In a 180-second, 24 fps render, all 4,320 final per-frame source descriptions were regenerated and hashed after a patch. Source-content differences invalidated 768 frames; 3,552 unchanged descriptions reused raster frames only after their stored raster hashes were checked. The delivered sequence was then fully decoded and compared with the final source rasters. This illustrates content-based invalidation, not a fixed rerender percentage or a permission to reuse frames with changed renderer settings. Preserve the renderer/configuration/resource provenance too. Source consistency does not prove explanatory accuracy or listening quality.

## Normal-playback observation limits

Verify the actual playback starting position; clicking a timeline is not proof of returning to zero. Record the viewed intervals, timing basis, gaps, UI-only observations and repeated end frames. A wall-clock span longer than the film does not establish continuous coverage, and desktop capture times are not exact source PTS. Treat independent decoded-frame reviews, action strips, normal-speed sampled observations and actual listening as distinct evidence.

For example, a normal-playback sample review of a 180-second sequence had an 11.645-second observation gap at a capture-call boundary. Separate decoded comparisons can support checks of the affected content, but cannot retroactively make that normal-playback record gap-free. A review of the silent version can inform the music version's visuals only when video-frame equivalence is verified; it says nothing about audible joins, harmony or listening comfort. Unheard audio remains not_checked even if loudness, clipping, stream duration and audio hashes pass. Delivery of a file is not platform submission, moderation or public availability.

## Gap-directed normal-speed review

After an initial whole-film playback, use the observation record to identify specific uncovered intervals or unresolved transitions. Review those intervals at normal speed with enough preceding and following context to judge the action and caption. Record the newly observed scope and remaining gaps; do not repeatedly replay the whole film as a substitute for resolving a known gap. A seek target is not an observed media timestamp, and UI-only captures or repeated end frames add no film coverage. Where precise timing is unavailable, preserve that uncertainty instead of reporting exact decoded coverage. These are review recommendations, not evidence that any particular film has passed them.

## Close specific review risks without widening the claim

Define the unresolved risk and the evidence needed before another review pass. Static samples may settle visible content at those samples; they do not settle motion, flicker, reading comfort or an earlier normal-playback gap. Repeated source images can match several media times, so retain a candidate interval rather than infer an exact screenshot PTS from image similarity or wall-clock differences.

When suitable evidence resolves the specified transition or visibility risk and reveals no new defect, close that item instead of replaying the same window indefinitely. Do not turn proof of uninterrupted observation of every frame into a universal prerequisite for all local QA decisions. Retain untested claims separately and recheck affected scope after changes. This does not waive final-file decoding, output identity checks, required normal-speed review or actual listening when those belong to the deliverable.

## Camera tests: synthetic counterexamples versus actual inputs

Keep synthetic boundary tests separate from tests using an example's actual geometry and camera timeline. A synthetic threshold crossing can expose a discontinuous velocity without proving that the original shot ever enters that branch. Test one-sided changes at thresholds and keyframe endpoints, stating time steps and projection units; symmetric differences can hide a jump. If a constraint is smoothed, retest the protected region rather than assume its safety guarantee survives.

A scoped numerical study of Lemo's one-line example at [revision 413a6bd6d78ebd3bdd5abaec9538a26867f890df](https://github.com/lemomo-ai/lemo-opuscar/tree/413a6bd6d78ebd3bdd5abaec9538a26867f890df) used actual path and camera data but replaced DOM path measurement with a CPU Bezier approximation. The sampled actual-input run did not trigger the pen-tip correction branch implicated by a separate synthetic example. This is an approximate numerical result, not original-renderer execution, a continuous-time proof or evidence of visible smoothness. Record replacement algorithms, tolerances and convergence; internal convergence is not an error bound against the original DOM implementation. Source and license boundaries remain in [attribution](attribution.md).

Separate pen-tip containment, the already-drawn centerline, the currently relevant object, full ink/stroke extents, labels and actual viewing. Camera-follow coordinates need not equal the displaced drawing coordinates. A close-up need not contain every historical or future path; a full reveal must check the set relevant to that shot. A centerline bounding box excludes stroke width, shadows and other effects, so it cannot certify complete visual safety.

## Endpoint handoffs and occlusion regressions

When a result moves between subjects, preserve the source and destination identities and the source result. Animate an identifiable copy from the source, through the channel and into the destination before revealing its readable result. Shared color alone does not establish provenance. Preserve the model's semantics throughout: content readable at endpoints need not be readable in transit, and a received result must not replace the destination's identity label. An explanatory handoff does not establish additional protocol or physical behavior.

Two useful failure patterns are a moving enclosure crossing the very source text it explains, and a faint destination guide crossing text while that text appears. Route the moving shape around the actual rendered ink, and end the guide before the reveal begins when that avoids the collision. Low opacity is not an exemption from readability checks.

Use real glyph/ink bounds rather than an estimated text anchor. Check the new shape, outline and relevant effects across the affected rendered frames with a documented screen-space clearance. State which objects were tested; zero intersections in those frames is not continuous-time proof or whole-layout approval. Inspect full-size and mobile-size output plus contextual normal-speed motion: a geometric pass alone cannot establish a comprehensible handoff. Preserve the failed attempt, the corrective diff and the final recheck separately. If capture fails or collects only an ended player's UI, exclude those observations; identify the final artifact in a valid retry rather than crediting an earlier version.

Keep three reuse claims distinct: unchanged source descriptions, unchanged source rasters and unchanged encoded video bytes. Re-encoding a full lossy stream does not preserve all unaffected encoded frames byte-for-byte. An unchanged audio payload does not establish listening, and a local visual improvement does not close another deliverable's missing review.

## Optional procedural audio: static findings

These are revision-bound source-reading findings from Lemo's [core/audio/sfx.py](https://github.com/lemomo-ai/lemo-opuscar/blob/413a6bd6d78ebd3bdd5abaec9538a26867f890df/core/audio/sfx.py), not execution or listening results. No upstream audio code or media is bundled. This section does not prescribe adding sound effects or narration to a brief that excludes them.

- A module-global random generator seeded once gives reproducibility only for the same initialization and draw sequence, not independent event regeneration. Randomized functions consume shared state; even an extra call made to obtain a length can consume random values. In this revision, heartbeat makes an additional noise-consuming thump call to obtain a length. This is a static inference, not an executed regression.
- For an adaptation, derive an independent generator from a stable event ID, master seed and parameter version using a stable digest, or freeze each event's generated PCM and content hash. Do not use a process-randomized built-in hash as the stable identity. Keep the event manifest shared with visual timing while preserving visible causality without sound.
- Test the same event in forward, reverse, isolated and segmented generation, then insert an unrelated event and compare existing event PCM. Lock mix summation order and precision separately: event determinism does not guarantee bitwise equality under arbitrary floating-point accumulation order. These are proposed tests, not tests already passed.
- Inspect executable contracts, not the header alone: this revision's add function mutates a stereo buffer, while the header describes mono float32 return values; default NumPy paths do not uniformly cast float32. Validate shapes, dtype, finite values, panning bounds, timing-to-sample rounding and an explicit policy for cropped starts or discarded tails.
- Validate empty arrays and short/zero windows before calling normalization, brown-noise or limiter helpers. A limiter's name does not establish true-peak safety. Measure the encoded output and actually listen separately; source inspection establishes neither safe peaks nor a satisfactory mix.

Status here is source_read only. Adaptation, runtime regression, encoded-audio validation and listening remain not_checked. The [Lemo MIT notice](licenses/LemoLab-MIT.txt) remains applicable to its code/documentation; it does not grant rights to example recordings or third-party assets.

## Actual-font caption boundaries

Space-based word wrapping does not handle continuous Chinese or an overwide first token. Do not use character count or a text anchor as an ink-width measurement, or silently split a number/identifier to make a test pass. Preserve the original text and its deliberate rendered lines, then measure the actual installed font in the actual renderer.

For trusted project-generated static SVG, `scripts/check_caption_bounds.py` uses installed Inkscape and Fontconfig (`fc-match`). It does not install dependencies or execute a film renderer. Supply a JSON manifest:

```json
{"samples":[{"id":"caption-1","svg":"frames/example.svg","text":"原句","lines":["原句"],"safe_rect":[0,0,960,540]}]}
```

Run from the directory against which SVG paths resolve:

```sh
python scripts/check_caption_bounds.py manifest.json --output bounds.json
python -m unittest discover -s scripts -p 'test_caption_bounds.py' -v
```

Each line must identify exactly one SVG `text` element and explicitly declare one installed font family. The helper records the requested font, resolved family/style, font file hash and source SVG hash, then queries ink boxes on a temporary copy. Use ordinary Regular/Bold font styles; the small helper is not a general CSS, variable-font, inherited-style or browser-layout engine. A primary font match does not prove that every Unicode glyph avoided internal fallback. The result includes local file paths: keep production result manifests private, and sanitize them before any sharing.

`safe_rect` is the actual intended region in SVG user coordinates, not an inferred platform safe area. Choose the correct canvas or subtitle bar separately for each layout. Check all four edges; a missing font, ambiguous line, malformed input or absent box is unverified, not a pass. Fix incorrect test-region inputs without moving valid subtitles to satisfy a wrong rectangle. The checker rejects selected active/external SVG constructs but is **not a sanitizer or security boundary**: only feed trusted static SVG, not arbitrary downloaded files or stylesheets.

A sample pass establishes containment only at that sample. It does not cover every frame, opacity transitions, animated occlusion, mobile readability, actual reading speed, listening, rights or release permission. Keep those checks separate and state uncovered intervals. The included 17 regressions cover finite rectangles, all edges, exact text, ambiguous matching, active-element rejection, missing fonts and actual-font Chinese/long-token overflow. Empty/non-list sample collections, non-object rows and malformed JSON/root values produce unverified results and a nonzero CLI exit, never an empty pass. Their font-dependent tests require Inkscape, Fontconfig and Noto Sans CJK SC; unavailable dependencies are not a test pass.

### Source-derived layer and state contracts

Static reading of Lemo's pinned `styles/blueprint/demo/sheet.js` suggests keeping subject outlines, internal light/dark masks and mechanism overlays separate. Clip shading to the subject rather than darkening the entire frame. Drive shadow offset, blur and strength from one shared lift state, while retaining a common projection. These are stylized mappings, not physical height or PBR verification. Preserve/restore compositing state, validate dimensions and zoom, and test camera changes before claiming reusable rendering behavior. The source's space-only wrapping motivated the independent caption checker above; no upstream renderer is bundled or executed by it.
