#!/usr/bin/python3
import telepot
import argparse
import textwrap


def set_args():
    parser = argparse.ArgumentParser(
        description='Get chat id of telegram bot.')
    required = parser.add_argument_group('required arguments')
    required.add_argument(
        '-t', '--token', help='telegram bot token', required=True)
    parser.add_argument('-c', '--get_chat_id', action="store_true",
                        help="Retrieve ID of chat (send a message to the bot first)")
    parser.add_argument(
        '-i', '--chat_id', help="ID of the chat with the bot. (-c to find it first)")
    parser.add_argument('-N', '--torrent_name', help="Torrent name")
    parser.add_argument('-L', '--category', help="Category")
    parser.add_argument('-G', '--tags', help="tags")
    parser.add_argument('-F', '--content_path',
                        help="Content path (same as root path for multifile torrent)")
    parser.add_argument('-R', '--root_path',
                        help="Root path (first torrent subdirectory path)")
    parser.add_argument('-D', '--save_path', help="Save path")
    parser.add_argument('-C', '--number_of_files', help="Number of files")
    parser.add_argument('-Z', '--torrent_size', help="Torrent size (bytes)")
    parser.add_argument('-T', '--current_tracker', help="Current tracker")
    parser.add_argument('-I', '--info_hash', help="Info hash v1")
    parser.add_argument('-J', '--info_hash2', help="Info hash v2")
    parser.add_argument('-K', '--torrent_id', help="Torrent ID")
    args = parser.parse_args()
    return args


def get_chat_id(token):
    bot = telepot.Bot(token)
    response = bot.getUpdates()

    try:
        for obj in response:
            print(obj['message']['chat']['id'])
    except KeyError:
        print("An exception occurred. Check if your token is correct")

    print(response)


def send_message(token,
                 chat_id,
                 torrent_name,
                 category=None,
                 tags=None,
                 content_path=None,
                 root_path=None,
                 save_path=None,
                 number_of_files=None,
                 torrent_size=None,
                 current_tracker=None,
                 info_hash=None,
                 info_hash2=None,
                 torrent_id=None):

    bot = telepot.Bot(token)
    template = """*Torrent finished downloading*
Name: {torrent_name}
""".format(torrent_name=torrent_name)

    if category is not None:
        template += """Category: {category}
""".format(category=category)
    if tags is not None:
        template += """Tags: {tags}
""".format(tags=tags)
    if content_path is not None:
        template += """Content Path: {content_path}
""".format(content_path=content_path)
    if root_path is not None:
        template += """Root Path: {root_path}
""".format(root_path=root_path)
    if save_path is not None:
        template += """Save Path: {save_path}
""".format(save_path=save_path)
    if number_of_files is not None:
        template += """Number of files: {number_of_files}
""".format(number_of_files=number_of_files)
    if torrent_size is not None:
        template += """Torrent Size: {torrent_size}
""".format(torrent_size=torrent_size)
    if current_tracker is not None:
        template += """Current tracker: {current_tracker}
""".format(current_tracker=current_tracker)
    if info_hash is not None:
        template += """Info Hash v1: {info_hash}
""".format(info_hash=info_hash)
    if info_hash2 is not None:
        template += """Info Hash v2: {info_hash2}
""".format(info_hash2=info_hash2)
    if torrent_id is not None:
        template += """Torrent ID: {torrent_id}
""".format(torrent_id=torrent_id)

    message = template.strip()
    bot.sendMessage(chat_id, message, parse_mode='Markdown')


def main():
    args = set_args()
    if args.get_chat_id:
        get_chat_id(token=args.token)
    else:
        send_message(token=args.token,
                     chat_id=args.chat_id,
                     torrent_name=args.torrent_name,
                     category=args.category,
                     tags=args.tags,
                     content_path=args.content_path,
                     root_path=args.root_path,
                     save_path=args.save_path,
                     number_of_files=args.number_of_files,
                     torrent_size=args.torrent_size,
                     current_tracker=args.current_tracker,
                     info_hash=args.info_hash,
                     info_hash2=args.info_hash2,
                     torrent_id=args.torrent_id)


if __name__ == "__main__":
    main()
