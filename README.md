<p align="center">
<img src="./dtlogo.png" alt="Duckietown Logo" width="50%">
</p>

# **Duckietown Learning Experiences (LX)**

# About this repository

This is a Duckietown learning experiences repository containing activites compatible with the Duckietown infrastructure. Visit us at the 
[Duckietown Website](https://www.duckietown.com) for more learning materials, documentation, and demos.

# Setup

To use these learning experiences do the following:

## Step 0 - Requirements

We assume here that you have already set up your Duckietown development environment 
following the steps in the 
[Laptop setup](https://docs.duckietown.com/daffy/opmanual-duckiebot/setup/setup_laptop/index.html) and [Accounts setup](https://docs.duckietown.com/daffy/opmanual-duckiebot/setup/setup_account/index.html)
sections of the of the Duckietown operation manual.

<!--
```{todo}
absolute URL
```
-->

Add your `docker.io` credentials to `dts` by running the following command,

```
dts challenges config --docker-username <USERNAME> --docker-password <PASSWORD>
```

**NOTE:** these are the `<USERNAME>` and `<PASSWORD>` you use to login on DockerHub (hub.docker.io).


## Step 1 - Installation

Start by installing a new dependency,

    sudo apt install libnss3-tools

Then update your Duckietown shell and shell commands,

    pip3 install -U duckietown-shell

    dts update

## Step 2 - SSL certificate

Next, set up your local SSL certificate needed to run the learning experience editor,

    dts setup mkcert

**Note**: if you are trying to run the lx with the experimental setup on WSL you need to install `mkcert` on Windows before running the `dts setup mkcert` command. Follow these steps by running the commands in an _administrative PowerShell_:

1. Install Chocolately: ```Set-ExecutionPolicy Bypass -Scope Process -Force;  [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072;
iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))` ```
2. Install `mkcert`: ```choco install -y mkcert```
3. Set WSL to use the Windows Certificate Authority of `mkcert`: ```$env:CAROOT="$(mkcert -CAROOT)"; setx CAROOT $env:CAROOT; If ($Env:WSLENV -notlike "*CAROOT/up:*") { $env:WSLENV="CAROOT/up:$env:WSLENV"; setx WSLENV $Env:WSLENV }```
4. Reboot your Windows machine.

## Step 3 - Fork this repository

To store your own code, while also keeping the ability to pull updates from our version of this repo, create your own fork.

Start by pressing "Fork" in the top right corner of this repository page on GitHub. You will be able to create a new 
fork: `<your_username>/duckietown-lx`

Then clone your new repository, replacing your GitHub username in the command below,

    git clone -b duckiedrone-lxs git@github.com:<your_username>/duckietown-lx

## Step 4 - Set up the remote

Now we will configure the Duckietown version of this repository as the upstream repository to sync with your fork.

List the current remote repository for your fork,

    git remote -v

Specify a new remote upstream repository,

    git remote add upstream https://github.com/duckietown/duckietown-lx

Confirm that the new upstream repository was added to the list,

    git remote -v

You can now push your work to your own repository using the standard GitHub workflow, and the beginning of every 
exercise will prompt you to pull from the upstream repository - updating your exercises to the latest Duckietown 
version,

    git pull upstream duckiedrone-lxs

## Step 5 - Set up the GitHub credentials

To upload code to your GitHub account from inside the LX you will need to setup a GitHub Token in dts.

1. You can generate a token following [these instructions](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-personal-access-token-classic).

1. Once you have generated your token you can add it to the _dts credentials manager_ by running:

    dts config github credentials set --username YOUR_GITHUB_USERNAME --token YOUR_GITHUB_TOKEN

Now you will be able to push and pull to your repo from inside the editor.

## What next?

You will find the following set of instructions in every individual directory in this repository. This 
workflow will allow you to build and test your code, run solutions in simulation and on the [Duckiebot](https://get.duckietown.com/collections/dt-robots/products/duckiebot-db21?variant=41543707099311), and submit your 
work to the [challenges server](https://challenges.duckietown.org/) to evaluate it.

# Instructions

**NOTE:** All commands below are intended to be executed from the root directory of a single exercise (e.g., the 
`braitenberg` directory).

## 1. Make sure your folder is up-to-date

Update your folder definition and instructions,

    git pull upstream duckiedrone-lxs


## 2. Make sure your system is up-to-date

- 💻 Always make sure your Duckietown Shell is updated to the latest version. See [installation instructions](https://github.com/duckietown/duckietown-shell)

- 💻 Update the shell commands: `dts update`

- 💻 Update your laptop/desktop: `dts desktop update`

- 🚙 Update your Duckiebot: `dts duckiebot update ROBOTNAME` (where `ROBOTNAME` is the name of your Duckiebot chosen during the initialization procedure.)


## 3. Work on the exercise

### Launch the code editor

Open the code editor by running the following command,

```
dts code editor
```

Wait for a URL to appear on the terminal, then click on it or copy-paste it in the address bar
of your browser to access the code editor. The first thing you will see in the code editor is
this same document, you can continue there.


### Walkthrough of notebooks

**NOTE**: You should be reading this from inside the code editor in your browser.

Inside the code editor, use the navigator sidebar on the left-hand side to navigate to the
`notebooks` directory and open the first notebook.

Follow the instructions on the notebook and work through the notebooks in sequence.


### 💻 Testing in simulation

**note:** this is not yet available in the Duckiedrone exercises.

To test in simulation, use the command

    dts code workbench --sim

There will be two URLs popping up to open in your browser: one is the direct view of the
simulated environment. The other is VNC and only useful for some exercises, follow the instructions
in the notebooks to see if you need to access VNC.

This simulation test is just that, a test. Don't trust it fully. If you want a more accurate
metric of performance, continue reading to the `Perform local evaluation` section below.

### ℹ️ Check Robot Compatibility
While we try our best to support running these exercises on all versions of the Duckiebot, some activities require special hardware and
are only supported on specific robots. Please use this section to ensure the compatibility of the exercise and your 
robot.

The support matrix of this exercise is as follows:

| Duckiebot Type   	                                                                                | Configuration 	 | Support Level   	    |
|---------------------------------------------------------------------------------------------------|-----------------|----------------------|
| [DB21-J4](https://get.duckietown.com/products/duckiebot-db21?variant=41543707099311)            	 | Jetson 4GB    	 | ✔️ Full Support    	 |
| [DB21-J2](https://get.duckietown.com/products/duckiebot-db21?variant=40700056830127)            	 | Jetson 2GB    	 | ⚠️ Partial Support 	 |


### 🚙 Testing on a physical robot

**note:** in the Duckiedrone exercises you will have different instructions to follow.

You can test your agent on the robot using the command,

    dts code workbench --duckiebot YOUR_DUCKIEBOT

This is the modality "everything runs on the robot".

You can also test using

    dts code workbench --duckiebot YOUR_DUCKIEBOT --local 

This is the modality "drivers running on the robot, agent runs on the laptop."


### 📽 Perform local evaluation

We suggest you evaluate your work locally before submitting your solution.
You can do so by running the following command,

    dts code evaluate

This should take a few minutes.
This is not supposed to be an interactive process: just let it run, and when you return,
you will find the output in a folder, including videos, and trajectories, and all the statistics
you would usually find on the [challenges website](https://challenges.duckietown.org/).


### 📬 Submit your solution

When you are ready to submit your homework, use the following command,

    dts code submit

This will package all your code and send it to the Duckietown servers for evaluation.


## Troubleshooting


If an error of this form occurs

```bash
Traceback (most recent call last):
  File "/usr/local/lib/python3.8/dist-packages/duckietown_challenges_cli/cli.py", line 76, in dt_challenges_cli_main
    dt_challenges_cli_main_(args=args, sections=sections, main_cmd="challenges")
  File "/usr/local/lib/python3.8/dist-packages/duckietown_challenges_cli/cli.py", line 203, in dt_challenges_cli_main_
    f(rest, environment)
  File "/usr/local/lib/python3.8/dist-packages/duckietown_challenges_cli/cli_submit.py", line 165, in dt_challenges_cli_submit
    br = submission_build(
  File "/usr/local/lib/python3.8/dist-packages/duckietown_challenges_cli/cmd_submit_build.py", line 41, in submission_build
    raise ZException(msg, available=list(credentials))
zuper_commons.types.exceptions.ZException: Credentials for registry docker.io not available
available:
```

you need to log into docker using `dts`. Use this command:

```
dts challenges config --docker-username <USERNAME> --docker-password <PASSWORD>
```


## Retire obsolete submissions

Note that you can "retire" submissions that you know are wrong.
You can do this through [the Duckietown Challenges website](https://challenges.duckietown.org/).

To do so, login using your token, then find the submission you want to retire from the list of submission
in your user profile page. Use the button "retire" to the right of the submission record line.
