powerline_ruby_segment
======================

A powerline segment to show which version or ruby you are currently running.
Simply copy into the powerline_shell folder and install powerline_shell (python setup.py install)

Don't forget to create a config file and to add ruby_segment to it, ex:

```
cat ~/.powerline-shell.json

{
  "segments": [
    "virtual_env",
    "ssh",
    "cwd",
    "git",
    "ruby_version",
    "hg",
    "jobs",
    "root"
  ]
}
```
