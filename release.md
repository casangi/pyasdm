# Releasing pyasdm

pyasdm is published to PyPI by the GitHub Actions workflow in
`.github/workflows/python-publish.yml`. The workflow runs whenever a GitHub
release is created and calls the shared NRAO template
`nrao/gh-actions-templates-public/.github/workflows/python-publish-cngi-template.yml`,
the same template XRADIO uses. The template builds a source distribution and
wheel with `python -m build` and uploads them to PyPI with the `PYPI_TOKEN`
secret.

The version that is published is the `version` field in `pyproject.toml`, not
the release tag. The tag and `pyproject.toml` must therefore be updated
together before every release.

## One time setup

These steps only need to be done once, before the first release.

1. Make the `PYPI_TOKEN` secret available to the repository. XRADIO gets it
   from the `casangi` organization. Ask an organization admin to add pyasdm
   to the repositories that can use the organization secret, or add a
   repository secret named `PYPI_TOKEN` under
   Settings > Secrets and variables > Actions > New repository secret.
   For the very first upload the token must be an account scoped PyPI token,
   because a project scoped token cannot be created until the project exists
   on PyPI.
2. Create the `release` environment used by the template under
   Settings > Environments > New environment, named `release`. No protection
   rules or environment secrets are required. If the environment does not
   exist GitHub creates it automatically on the first run, so this step is
   optional but keeps the deployment history tidy.
3. Check that the `pyasdm` name is available on PyPI (https://pypi.org/project/pyasdm).

## Standard release

1. Choose the new version number, for example `0.1.0`. Versions follow
   PEP 440 (https://peps.python.org/pep-0440/).
2. On `main`, set `version = "0.1.0"` in `pyproject.toml`, commit, and push
   (or merge through a pull request). Wait for the test workflows on that
   commit to pass.
3. On GitHub go to the repository page and click Releases, then
   Draft a new release.
4. Under Choose a tag, type the new tag `v0.1.0` and select
   Create new tag on publish. The tag must match the version in
   `pyproject.toml`, prefixed with `v`.
5. Under Target, select `main`.
6. Set the release title to the same string as the tag, `v0.1.0`.
7. Click Generate release notes and edit the generated text as needed.
8. Leave Set as a pre-release unchecked. Leave Set as the latest release
   checked.
9. Click Publish release.
10. Open the Actions tab and watch the run named
    "Publish Python distribution to PyPI and TestPyPI". When it finishes,
    confirm the new version is listed at https://pypi.org/project/pyasdm and
    install it with `pip install pyasdm==0.1.0`.

## Alpha release

An alpha release is used to publish a preview from a feature branch, or
from `main` ahead of a full release, without changing what
`pip install pyasdm` installs. pip ignores pre-release versions unless the
user asks for them explicitly with `pip install --pre pyasdm` or
`pip install pyasdm==0.1.0a1`.

1. Choose the alpha version. Use the version of the upcoming release with an
   alpha suffix, for example `0.1.0a1` for the first alpha of `0.1.0`, then
   `0.1.0a2` for the next one. (XRADIO uses the spelling `1.1.9-alpha`,
   which PEP 440 normalizes to `1.1.9a0`. Either spelling works, but the
   `a1`, `a2` form allows several alphas of the same version.)
2. On the branch you want to publish, set `version = "0.1.0a1"` in
   `pyproject.toml`, commit, and push.
3. On GitHub click Releases, then Draft a new release.
4. Under Choose a tag, type `v0.1.0a1` and select Create new tag on publish.
5. Under Target, select the branch to publish. This can be a feature branch;
   it does not have to be `main`.
6. Set the release title to `v0.1.0a1` and add a short description of what
   the alpha contains and why it exists.
7. Check Set as a pre-release. Make sure Set as the latest release is
   unchecked, so the alpha does not replace the current release on the
   repository front page.
8. Click Publish release.
9. Watch the run in the Actions tab and confirm the alpha appears under
   Release history at https://pypi.org/project/pyasdm/#history. Test it with
   `pip install pyasdm==0.1.0a1`.
10. Before the corresponding standard release, set `pyproject.toml` back to
    the final version, for example `0.1.0`.

## Troubleshooting

- The workflow only runs for the `created` release event. Editing an
  existing release, or converting a draft to published later, may not
  trigger it. If nothing runs, delete the release and its tag and create the
  release again.
- A version can only be uploaded to PyPI once. If the upload succeeded but
  something is wrong with the package, bump to a new version (for example
  `0.1.1`) and release again. Do not try to reuse a version number.
- The job fails immediately with "PYPI_TOKEN is EMPTY" if the secret is not
  available to the repository. See One time setup.
- The published version does not match the tag if `pyproject.toml` was not
  updated before the release was created.
