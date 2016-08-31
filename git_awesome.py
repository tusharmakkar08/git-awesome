__author__ = 'tusharmakkar08'

import sys
from subprocess import Popen, PIPE

import colorama


def _git_output_parser(error_data):
    suggestion_split = error_data.split('Did you mean')
    replaced_command = suggestion_split[0].split('git: \'')[-1].split('\' is not')[0]
    recommendation = suggestion_split[-1].split('?')[-1]
    recommendation_commands = [i.strip() for i in filter(None, recommendation.split('\n'))]
    return replaced_command, recommendation_commands


def _print_error(recommendation_commands, stderr_data):
    for index, command in enumerate(recommendation_commands):
        stderr_data = stderr_data.replace(command, colorama.Fore.RED + str(index + 1) + '.  ' + colorama.Fore.MAGENTA +
                                          command + colorama.Style.RESET_ALL)
    print stderr_data


def _return_modified_command(cmd, recommendation_commands, replaced_command):
    if len(recommendation_commands) > 1:
        response = raw_input(colorama.Fore.BLUE + "Which one do you mean ?\n" + colorama.Style.RESET_ALL)
        try:
            modified_command = ["git", cmd.replace(replaced_command, recommendation_commands[int(response) - 1])]
        except Exception:
            modified_command = -1
    else:
        single_command = ["git", cmd.replace(replaced_command, recommendation_commands[0])]
        response = raw_input(colorama.Fore.BLUE + "Do you want to run: " + colorama.Fore.YELLOW +
                             ' '.join(single_command) + colorama.Fore.BLUE + " ?\n" + colorama.Style.RESET_ALL).lower()
        if response.startswith('y') or response.startswith('1'):
            modified_command = single_command
        else:
            modified_command = -1
    return modified_command


def git_awesome(cmd):
    _, stderr_data = Popen(["git", cmd], stderr=PIPE).communicate()
    if len(stderr_data):
        replaced_command, recommendation_commands = _git_output_parser(stderr_data)
        _print_error(recommendation_commands, stderr_data)
        modified_command = _return_modified_command(cmd, recommendation_commands, replaced_command)
        if modified_command == -1:
            return
        print(colorama.Fore.GREEN + "Running: " + colorama.Fore.YELLOW + ' '.join(modified_command) +
              colorama.Style.RESET_ALL)
        _, stderr_data = Popen(modified_command, stderr=PIPE).communicate()
        if len(stderr_data):
            print(stderr_data)


if __name__ == '__main__':
    git_awesome(sys.argv[1])
