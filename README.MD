# pacdelta 
### Python scripts to generate delta updates for pacman
## Guidelines for use:
The scripts are pretty be simple to read. Understand them before using them. Nevertheless, here's a rough idea of how to make it work:

The core concept is this: you have a client that is bandwidth constrained and a server which is not, both are under your control and the client has pacman installed. You generate a list of "diff" of a sort between the current state of your pacman local cache and the state you want it to be in using the `checkupdates` tool. You move this diff to the server and have the server download both the versions existing in your cache and the latest versions. With both versions of the package available, the `zstd` project's patching engine is used to generate a patch to turn the old .zst package file into the latest one. Once all the patches have been generated, you download them onto the bandwidth constrained device and apply them to the outdated .zst files in you local pacman cache, filling the cache with the newest versions. It's kinda clumsy at this point but it works with some tinkering.
## Further Instructions
- Use the `checkupdates` tool from the `pacman-contrib` package to generate the list of updates to be done. Store this as the patches.txt file on the server alongside the .ipynb file.
- Use the notebook to generate and download a `patches.tar` file containing all the deltas and the associated .sig files.
- Use the `pacdelta.py` script (with edits if required) to apply the patches, the results are stored in the newdb folder.
- Copy the .zst files in newdb to your local pacman cache, usually found in `/var/cache/pacman/pkg`
- Sync and update with pacman as usual, hopefully it finds the patched files in the cache to be sufficient.
