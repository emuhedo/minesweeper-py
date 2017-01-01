from minesweeper import game


def main():
    help = game.Help()
    setup = game.Setup()
    loop = game.Loop()
    end = game.End()

    help.set_state(loop)
    setup.set_state(loop)
    end.set_state(setup)
    loop.set_states(setup, help, end)

    setup.setup()


if __name__ == "__main__":
    main()
