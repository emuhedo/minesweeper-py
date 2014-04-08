#!/usr/bin/python

import game

help = game.Help()
setup = game.Setup()
loop = game.Loop()
end = game.End()

help.setState(loop)
setup.setState(loop)
end.setState(setup)
loop.setStates(setup,help,end)

setup.setup()