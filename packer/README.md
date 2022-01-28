## File format

Sticker packs have their own file format for the installer app.

- Each sticker is in the WebP image format

- Each sticker is exactly 512x512 pixels

- Sticker packs contain between 3 and 30 of these stickers

- The pack contains `author.txt`, which contains the author's name in plaintext

- The pack contains `title.txt`, which contains the name of the pack in plaintext

- The pack contains `tray.png`, which is a 96x96 pixel PNG file of the tray icon

- The sticker pack itself is a ZIP file of all of the above files together (`author.txt`, `title.txt`, `tray.txt`, and all of the sticker image files)

Finally, while it's not a must, the sticker pack / ZIP file should have the extension `.wastickers`. This makes it so Android can automatically open the sticker pack in the installer app. 