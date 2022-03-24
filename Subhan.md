## Deploy
You can deploy this bot anywhere.

<details><summary>Deploy To Heroku</summary>
<p>
<br>
<a href="https://telegram.dog/XTZ_HerokuBot?start=RXZhbWFyaWFURy9FdmFNYXJpYSBtYXN0ZXI">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Deploy To VPS</summary>
<p>
<pre>
```sh
sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/subhan-1/TG-video-player # clone the repo.
cd video-Bot
pip3 install -U -r requirements.txt
cp example.env .env # use vim to edit ENVs
vim .env # fill up the ENVs (Steps: press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file).
python3 main.py # run the bot.

# continue the host with screen or anything else, thanks for reading.
```
