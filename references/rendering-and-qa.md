# Rendering and actual QA

Choose the visual medium deliberately: a watercolor character style is not a default for spatial 3D explanation; kinetic typography is not a vehicle-modeling system. Start with a treatment before reading a demo. Use a fixed seed and pure render(t), positive duration, explicit resource readiness and shared event/text/model state. World labels share the same projection transform as objects.

Distinguish implementation evidence: a working CPU SVG renderer, a browser WebGL/PBR renderer and an offline Cycles material still are separate capabilities. Report the one actually tested. Static approval does not establish motion, readability or audio quality.

Traffic objects must remain recognizable at mobile size: body silhouette, windows, wheels, front/back and ground contact; roads need surface, edges, markings and plausible width. Do not replace vehicles with tiny light beads without a stated abstraction appropriate to the task. Depth is conveyed by visible planes, light/shadow, occlusion, projection and contact, not a material name or dark filter.

For vehicles, consistently use the rear axle or center as the path reference. Derive steering from wheelbase and curvature; derive wheel rotation from traveled distance; inspect speed/curvature transitions and camera rate. Zero sampled collisions does not establish natural motion or continuous-time safety. Non-vehicle topics need not obey vehicle dynamics.

Retain a near-plane clipping regression: clip crossing triangles before projection, interpolate relevant attributes and verify materials/normals. Do not hide a disappearing-road defect through camera changes or a single-frame patch.

Review separately: model invariants; actual text bounds and fully-visible read time; full decode; full-size and 360px frames; per-shot contact sheets; action strips; cut-adjacent frames; normal-speed viewing; independent comprehension; audio listening. Mark each pass/revise/not_checked with exact scope and evidence. Playback time advancing, sampled screenshots, unique frames and successful decoding cannot substitute for continuous viewing. Unheard audio stays unchecked. Correct defects then inspect the actual revised output, not merely changed code.
