# Combined updates with Dependabot

GitHub's Dependabot tool is excellent. It periodically checks for updates in
your requirements, bumps them, and then opens a PR to run your tests and check
that all was passing.

Yay! 💃

It's bothered my for a while that it's too noisy though. For a big project with lots of dependencies you get a lot of commits in the history which aren't much more than book-keeping.

I've looked at batching the updates with `pip` — which is normally fine, but when you get a failure you need to work out which package it was that misbehaved, and TBH I'd much rather leverage someone else's tool that maintain even a simple GitHub action. (As ever, my favourite software is _No software_.)

I finally opened up the Dependabot docs, to see if there was a way around this. Sure enough, you can set a [target-branch option](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#target-branch) to have the individual updates applied there.

```yaml
  target-branch: "dependabot/combined"
```

I can then keep that rebased on `main` and make a combined updates PR periodically as desired.

That's more or less as smooth as I need it. 🦄
