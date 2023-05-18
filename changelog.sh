export PREVIOUS_VERSION=$(git tag -l --sort=-creatordate | head -n 1)
export CHANGES=$(git log --pretty="- %s" $PREVIOUS_VERSION..)
printf "# v${{ steps.current-version.outputs.version }}\n\n## Changes\n$CHANGES\n" > CHANGELOG.md