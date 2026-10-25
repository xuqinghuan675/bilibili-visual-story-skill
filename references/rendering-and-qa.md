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
