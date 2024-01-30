from interaction.interaction_utilities import sanitize

def write_log(message:str) -> None:
    with open('log.txt', 'a') as log_file:
        log_file.write(sanitize(message))

def clear_log() -> None:
    with open('log.txt', 'w') as log_file:
        log_file.write("")