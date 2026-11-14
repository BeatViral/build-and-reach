$ErrorActionPreference = 'Stop'
git subtree split --prefix site -b pages-publish-temp
if ($LASTEXITCODE -ne 0) { throw 'Could not create the publishing snapshot.' }
git push origin pages-publish-temp:gh-pages
if ($LASTEXITCODE -ne 0) { throw 'Could not push the publishing snapshot.' }
git branch -D pages-publish-temp
