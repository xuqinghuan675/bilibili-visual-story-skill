# Attribution and license boundaries

This package contains newly written project-method summaries and a scene-contract validator. It does not bundle upstream render engines, demos, reference media or internal assistant runtime skills. The following public projects informed the methods:

- Lemo, https://github.com/lemomo-ai/lemo-opuscar , reviewed revision 413a6bd6d78ebd3bdd5abaec9538a26867f890df: direction, technique, medium selection and deterministic rendering contracts. [MIT notice](licenses/LemoLab-MIT.txt).
- Howseen, https://github.com/howseen-ai/claude-motion-design , reviewed revision 3d90d349ef3fdde9b7e89de4df4a2159c9e8697f: independent visual description, cut-aware motion checks and diagnostic frame differences. [MIT notice](licenses/Howseen-AI-MIT.txt).
- John Heibel, https://github.com/JohnHeibel/ClaudeAnimationBase : painted-animation workflow. [MIT notice](licenses/John-Heibel-MIT.txt).
- tuzhechen2005, https://github.com/tuzhechen2005/opus-video-skills , reviewed revision 59744a69c7b916cfbe4c4ec84006b0c2f5e2fde1: shot-by-shot deterministic animation and render-and-look review. [MIT notice](licenses/opus-video-skills-MIT.txt).
- 3Blue1Brown, https://www.3blue1brown.com/lessons/linear-transformations/ : concrete visual continuity before abstraction. No scene code or media is distributed; scene repository licensing is distinct from the animation engine's license.
- HeyChengC, https://github.com/HeyChengC/vibe-knowledge-film : the public pigeon preview discussed in the study note. No reference media, code or original graphics is included.

Code/document licenses do not automatically cover demo films, screenshots, music, fonts or third-party assets. Lemo demo media is separately identified as CC BY 4.0 with exceptions; none is redistributed here. Preserved notices retain their original authorship and apply to their respective upstream work, not automatically to all new files. No new blanket license has been selected for this package's original files; the repository owner must choose one before representing broader reuse rights. Public visibility itself is not a license grant.


## Additional inspected sources and limits

Only newly written method summaries are included from the following research; no prompt bodies, renderer source, songs or example media are bundled.

- JohnHeibel/PDoomVideo, reviewed revision fa546a38092e75f2b079e6a86d6abc54dd525d17: https://github.com/JohnHeibel/PDoomVideo/tree/fa546a38092e75f2b079e6a86d6abc54dd525d17 . The inspected package metadata declares ISC but there is no standalone LICENSE file. Verify complete applicable terms before code reuse. Song provenance is not a commercial reuse grant. The existing John-Heibel-MIT.txt belongs to ClaudeAnimationBase, not this repository.
- yihui-dev/awesome-opus5-5-videos, reviewed revision 92aee2f586ac0715cb3cbcb6384834f98a33383d: https://github.com/yihui-dev/awesome-opus5-5-videos/tree/92aee2f586ac0715cb3cbcb6384834f98a33383d . Its MIT collection license does not establish rights to all linked creators' videos, music or characters. The inspected collection contains prompt text, not a runnable renderer or local example films; some transcriptions are partial or duplicated.
- joeseesun/opus-video-prompts, reviewed revision 7977c807781d4ba7c235247b8899a72575a30d00: https://github.com/joeseesun/opus-video-prompts/tree/7977c807781d4ba7c235247b8899a72575a30d00 . No repository LICENSE was found; documents retain original-author rights. Do not publicly copy full prompts. A collection or summary is not verification of its original author, complete prompt or generated result.
- A separate same-name collection exists at https://github.com/billyhetech/awesome-opus5-5-videos . Do not substitute it for yihui-dev or merge their reading coverage. Its credits distinguish collection licensing from authors' prompts and videos.
- The three visual reference authors and public video links are identified in [reference study](reference-study.md). They are study references, not a media reuse grant. No screenshots or video/audio files are distributed.

Lemo's code/document MIT notice does not cover all example audio: the specified Game Show Flat, Paper-cut Lightbox and Broadcast News Package voice assets have separate exclusions. Check file-level credits and licenses for fonts, samples, models and HDRI. A public-domain composition does not make a particular recording public domain.

Research remains partial: reading a style file or prompt collection does not mean its linked films were watched, its code ran or its outcome was reproduced. The fixed-reference quarter-second audit, normal-speed audiovisual review and full regression suite must not be labeled complete on the strength of these method notes. Repository names mentioning a model do not establish an actual model/API invocation.
