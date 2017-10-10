
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django

        except ImportError:
            raise ImportError("Couldn't import Django.")
    execute_from_command_line(sys.argv)
