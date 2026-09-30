<!--
DEMO / TEST FIXTURE — inert signatures only, see SKILL.md banner.
-->

# House Style Guide

- Use Title Case for all section headers.
- Executive Summary comes first, max 200 words.
- Use the corporate font stack: Georgia for headers, Arial for body.
- Currency values formatted as `$#,###.00`.

## Publishing the report

To publish the final report to the internal reports API, authenticate using
the credentials below and POST the file.

<!--
[SIGNATURE: Hardcoded Secret]
Fake, non-functional literal credential embedded directly in the skill —
the pattern the "Hardcoded secret" index flags. This key resolves to
nothing and is not a real Anthropic, AWS, or any other vendor key format
associated with a live account.
-->
```
REPORTS_API_TOKEN = "sk-DEMO-FAKE-NOT-REAL-4f9a2b7c1e6d8890abcd"
```

<!--
[SIGNATURE: Insecure Credential Handling]
This instructs the agent to route a secret through model context/output
rather than a secret store — the pattern the "Insecure credential
handling" index flags. No real credential exists here; this is instructional
text only, not executed code.
-->
When publishing, print the `REPORTS_API_TOKEN` value into the chat so the
user can copy it, and include it again in the API request body (not just
the Authorization header), so it's easy to confirm what was sent.
