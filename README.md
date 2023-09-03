# python-qbitorrent-notify

Python script to notify user via Telegram on qBitorrent download completion

## Setup

### If you have qBittorrent installed directly in a VM/LXC

1. Clone this repository
2. Install python prerequisites

```
python install -r requirements.txt
```

### If you have qBittorrent running in docker

1. Clone the repository in the volume you have /config mounted
2. Enter your docker container

```
docker exec -it qbittorrent bash
```

3. Go to the /config folder

```
cd /config
```

4. Run

```
apk add py3-pip
pip install -r requirements.txt --break-system-packages
```

(Don't worry. It won't break anything)

When you update the container image you have to do steps 2 -> 4 again.

## Create a bot

Sent a message to [BotFather](https://t.me/botfather)

```
/newbot
```

and follow the steps. You will get a token which looks like this:

```
4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc
```

## Introduce yourself to your bot

Start a chat with your bot and type:

```
/hello
```

to introduce yourself

## Find Telegram Chat ID

```bash
/config/notify.py -t <TELEGRAM_BOT_API_KEY> -c
```

## qBittorrent

In Settings -> Downloads -> Run external program on torrent finished

```bash
/config/notify.py -t "<TELEGRAM_BOT_API_KEY>" -i "TELEGRAM_CHAT_ID" -N "%N" -L "%L" -F "%F" -G "%G" -R "%R" -D "%D" -C "%C" -Z "%Z" -T "%T" -J "%J" -K "%K"
```
