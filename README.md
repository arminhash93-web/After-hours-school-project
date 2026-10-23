# 🎒 After Hours AI

A study space that runs entirely in your browser. It has an AI tutor, a focus timer, tasks, grades, flashcards, and a group chat with friends through Telegram or Bale.

**Live site:** `https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

## Pick your version

| Version | File | Group chat |
|---|---|---|
| US | `after-hours-ai-us.html` | Telegram |
| IR (نسخه ایران) | `after-hours-ai-ir.html` | Bale (بله) |

`index.html` is a front page that links to both. The two versions are identical apart from the chat service.

## Features

- **AI chat** in a ChatGPT-style layout, with saved conversations, chat search, tutor modes (Tutor, Math, Science, Writing, Coding, Languages, Explain like I'm 10), copy, regenerate, read aloud, voice input and export
- **AI shortcuts:** explain simply, quiz me, plan my night from your tasks, summarize notes, make flashcards
- **Focus timer** with presets, custom lengths, long breaks, a daily goal and a study streak
- **Tasks** with subjects, priorities, due dates and overdue warnings
- **Grades:** a weighted grade calculator, a "what do I need on the final" calculator, and a GPA calculator
- **Flashcards**, **notes**, a **week plan** and an **exam countdown**
- **Group chat** with friends through Telegram or Bale
- **Look and feel:** light and dark mode, preset or custom backgrounds, your own background image, accent color, text size and panel opacity
- **Backup:** copy your data as text and restore it later

## Setting up the AI

The AI tutor uses your own API key. Open **Settings → AI connection**, pick a provider, paste your key, and press **Test**.

Free options include Google Gemini (aistudio.google.com), Groq (console.groq.com) and OpenRouter (openrouter.ai). Free plans and model names change, so if a model stops working, type a different model name into the Model box.

Your key is saved only in your own browser. It is never uploaded anywhere except to the provider you choose. Don't share your screen or a saved copy of the page after entering a key.

## Setting up the group chat

### Telegram (US version)

1. In Telegram, message **@BotFather**, send `/newbot`, and choose a name and a username ending in `bot`. Copy the token.
2. Create a group, add your bot, and send a message in it.
3. If the bot can't see messages, send `/setprivacy` to @BotFather, pick your bot and choose **Disable**. Making the bot a group admin also works.
4. In the app's Telegram chat tab, paste the token, enter your name, press **Find chats**, choose your group, then press **Connect**.

### Bale (IR version)

1. In Bale, message **@botfather**, create a bot with `/newbot`, and copy the token.
2. Create a group, add the bot, and send a message in it. Making the bot a group admin can help it see messages.
3. Browsers usually block web pages from reading Bale directly, so run the relay on your own computer:
   ```
   python relay.py
   ```
   Leave that window open.
4. In the app's Bale chat tab, paste the token, enter your name, type `http://127.0.0.1:8787` in **Relay address**, press **Find chats**, choose your group, then press **Connect**.

`relay.py` only listens on your own computer. It passes requests to Bale and adds the headers the browser needs. Use `python relay.py telegram` if you ever need it for Telegram.

Only one copy of the app should be connected to a bot at a time, or the copies will take each other's messages.

## Running it yourself

No install is needed. Download the files, put them in one folder, and double-click `index.html`. Chat for Bale needs Python and `relay.py`.

To publish it with GitHub Pages: upload the files to your repository, go to **Settings → Pages**, choose **Deploy from a branch**, pick `main` and `/ (root)`, and save.

## Privacy and limits

- All data (tasks, notes, chats, settings, keys and tokens) is stored in your browser's local storage on your own device. Nothing is stored on a server by this project.
- Each version saves its own data separately. Use **Settings → Backup** to move notes and tasks. Backups leave out your keys, tokens and background image.
- Messages you send to the AI go to the AI provider you choose. Some free plans may use them for training, so don't paste anything private.
- The online Bale version may not be able to reach `relay.py` in every browser. If it doesn't work, run the downloaded file instead.
- Only chat with people you know, and don't share personal details in group chats.

## Files

| File | Purpose |
|---|---|
| `index.html` | Front page linking to both versions |
| `after-hours-ai-us.html` | The app with Telegram chat |
| `after-hours-ai-ir.html` | The app with Bale chat |
| `relay.py` | Small local helper for Bale (and optionally Telegram) |
