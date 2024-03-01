import sound.effects.echo
import sound.formats.wavread

# https://github.com/cwapi3d/cwapi3dpython/discussions/118

if __name__ == '__main__':

    print("module_sound.py is executed as main program")
    sound.effects.echo.test_echo()
    sound.formats.wavread.test_format()
