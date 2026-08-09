# DeepSeek Provider Profile

Classification: model API provider
Repository verification: `provider_only`

Official documentation: https://api-docs.deepseek.com/

DeepSeek can be used behind a direct API harness or a compatible runtime/switchboard. It does not natively discover `AGENTS.md`, task manifests, memory, skills, or outputs.

Keep the API key in an environment variable or approved secret store. Resolve the current base URL, protocol, model ID, context limits, tool support, and pricing from official documentation at execution time. The calling runtime owns context assembly, tool permissions, persistence, validation, and closeout.

Provider smoke and runtime adapter smoke are separate tests.
