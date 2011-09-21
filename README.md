Sync your Kindle clippings to Evernote when you connect your Kindle.

## Description
The python script can be used as a stand-alone script or in the attached Automator workflow (OSX only). The advantage of using the workflow is that it will automatically sync your stuff whenever you attach your Kindle to your Mac.

All notes for a book are stored in one note named after the title of that book and it's author and are tagged with `kindle-note`.

## Usage
Before running the script, please change the path where your clippings file is saved on your disk. The workflow automatically copies your clippings file from your Kindle to `~/Dropbox/kindle-clippings.txt`.
### Stand-alone
In your terminal, do this:
`python KindleEvernoteSync.py`
### As Automator workflow
Open the workflow in Automator and run it or assign it straight to your `/Volumes` directory on your Mac by right-clicking the `/Volumes` directory in Finder and click 'Folder Actions Setup'

Based upon [this gist](https://gist.github.com/1071682) by jplattel and [this workflow](http://evansims.com/1380/a-perfect-instapaper-sync-for-kindle/) by Evan Sims 
