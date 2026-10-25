# Scene contract v1

Top-level: version=1, project, integer seed, delivery=preview or publish, music and scenes. Music mode is none, external or platform; embedded is boolean. Non-silent modes require selected_title. Embedded external music requires cleared license_status and license_evidence. Platform publication requires platform_track_id and platform_terms_verified=true.

Publication requires publish_authorized=true, nonempty authorization_scope, qa_status=pass, reference_condition_met=true and content_updated=true. These are records of verified facts and valid authority, not authorization created by the validator. No fixed user style approval is assumed.

Each scene: unique id, start, positive duration, question, claim, source, visual_change, model_boundary, objects with unique IDs, persistent_ids, beats and positive hold_after_event. Scenes are contiguous. Persistent IDs must exist in both adjacent scenes; otherwise explain transition_reason. Beats have ordered local at times, object_id, action and explanatory reason, and leave sufficient time for the final hold. Timing and object checks do not verify mathematics, artistry, rights or comprehension.
