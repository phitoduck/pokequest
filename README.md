# Hello, Faith

This is a model project that you can copy and base all your python projects off of. When you've filled out this game, you can consider yourself a baller 🏀 python coder 😄.

This document you're reading is called a `README`. It's like a pretty explanation of a programming project.
It comes from the file `README.md`. Notice that it's one of the files in this `git repository`-- a folder
with a bunch of code files in it.

Git repositories are a nice way of uploading your code to the cloud in case you want to share it with other people. They're great for project portfolios, staying organized, showing off your code, and working on code with more
than one person.

## Instructions

It's totally fine if these instructions don't make sense. Following them blindly
will lead you to success!

### Step 1 (onetime) - `clone` this `repository`

`clone` just means download a copy
`repository` just means this folder with all the files in it

1. install git if you don't have it on your computer. `git` is a command that downloads this folder.
   1. Open up `iTerm` on your mac
   2. Check if `git` is installed (just type in `git --version`). You'll know if it didn't work.
   3. If it didn't work, install `git`. (type `brew install git`) Ta-da! The last step should give a different result now.

2. Do you see the big green button above that says `⬇️ Code`? Click that and copy that link. We'll call it `<link>`.
In iTerm--we're going to start calling that `your terminal`--do these commands:

```bash
# "cd" into whichever folder on your computer you want to download this repository to.
# "~/Desktop" this is the path to your desktop, if you want it to go somewhere else, 
# right click on that folder on your computer, hold down OPTION (look for this symbol: ⌥),
# and click the "Copy <blah> as Pathname" option, then use that path instead of "~/Desktop"
cd ~/Desktop 

# clone this repository to that folder. Replace <link> with the https://... thing that you copied
git clone <link>
```

### Step 2 (onetime) - Setup a `virtual environment`

The point of this step is to create a copy of python inside your copy of the `pokequest` repository.

1. `cd` into your `pokequest/` folder. You might have it in `~/Desktop/pokequest`.
2. Run `python3 -m venv pokequest-python/`. You should now have a folder named `pokequest-python/` in `pokequest/`

### Step 3 (everytime you code) - Activate your virtual environment

1. `cd` into your `pokequest/` folder.
2. Run: `source python/bin/activate`. You should not have a `(pokequest-python)`, in your terminal before your name and such. This means that any python code you run will be run with the `pokequest-python` copy of the python language. Good stuff.

### Step 4 (onetime) - `"Install"` this repository into `pokequest-python`

Okay seriously, `"repository"` is too long to type. We're going to start calling it a `repo` like the rest of the world 😄.

```bash
# with pokequest-python enabled (from step 3)
python3 -m pip install -e ".[all]" # meh... you learn what this command is soon enough
```

If you saw no errors after running that guy ^^^, the hard part is over!


### Step 5 (onetime) - Make `VS Code` **AWESOME**

`iTerm` is cool, but `VS Code` has a terminal, too, so we'll use that one from now on.

1. Open up `VS Code` with `pokequest` as a `"Workspace"`. It's pretty easy. Just open up `VS Code`, and there should be a button that says `Open Folder` or something...
2. Install a bunch of "Extensions" from the extension store. The extension store is on the lefthand sidebar. If you can't find it, you can open it up with `SHIFT` + `COMMAND` + `X`.
3. You can paste the list of extension id's below into the search bar to see the ones I like to use. Go ahead and install them all. You can read their little description pages if you want to get a feel for what they're about. That's not necessary though.

Extension Ids:
```bash
ms-python.python njpwerner.autodocstring bmuskalla.vscode-tldr mechatroner.rainbow-csv designbyajay.bash-cli-snippets aaron-bond.better-comments coenraads.bracket-pair-colorizer naumovs.color-highlight ms-vsliveshare.vsliveshare yzhang.markdown-all-in-one ibm.output-colorizer christian-kohler.path-intellisense hoovercj.vscode-power-mode oderwat.indent-rainbow naumovs.color-highlight ms-python.vscode-pylance
```

### Step 5 (onetime) - Tell `VS Code` about your copy of python

This step is so good. Once you do this, `VS Code` will be able to give you hints and even be able to autocomplete
some parts of your code as you type.

In the `VS Code` sidebar (in the file viewer with is the top option), you should see a folder named `.vscode`. In that folder, there is a file called `settings.json`. This is where all of the... settings are. I've set it up with
my favorite settings, and commented out some settings that you might want someday (but not yet). The comments in that file are the `//` lines.

See this line?

```json
"python.pythonPath": "PASTE YOUR VIRTUAL ENVIRONMENT PATH HERE. Use pipenv --venv or look into python -m venv"
```

You might notice that it wants you do change that setting. This is the path to the `pokequest-python` copy of python. Just right click the `pokequest-python/` folder in the sidebar and click `Copy Path`. Paste it in there, so 
it should look like:

```json
"python.pythonPath": "/Users/faith/and/her/path/to/pokequest-python"
```

Save the file. AND. YOU. ARE. DONE!