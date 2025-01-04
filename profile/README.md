# build-and-test

For every software repo in the world, you should be able to clone it onto a clean machine and run the "build and test" script at the root and it just works. 

No need to install something else first.

No need to understand how to invoke whatever build system it uses. 

Here you will find repos that demonstrate techniques for making this happen.

# Also

## Isolation

If you do this with two repos, or the same repo synced to an old state and a new state, they should not interfere with each other.
This means any tools and dependencies should be isolated, not shared system-wide.

## Repeatability

If we do this on two different machines or at two different times, the results should be the same.
This means that tools and dependencies should be pinned.

## Upgrades

It should be easy and obvious how to update pinned dependencies.
See `update_dependencies.md` in each repo for instructions.

## CI synchronization

CI and local builds should behave the same way, so that if an error appears in CI it's easy to reproduce it locally.
Typically this means that CI just runs the build-and-test script.
This also keeps CI configuration simple.

# Compromise

These are lofty goals, often impossible to meet with absolute perfection.
Each example compromises to some degree.
When picking a solution, select the compromises that are most acceptable for your context.

# Contributions

You probably know more about one of these languages/platforms/tools than I do and can see a way to make things better.
I would be so greatful if you would send a pull request or open an issue whenever you see such an opportunity.
