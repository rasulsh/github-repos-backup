# github-repos-backup
بک آپ گیری از تمام ریپو های یک اکانت

با استفاده از این اسکریپت می توانید به حساب کاربری خودتان در گیتهاب لاگین کرده و تمام ریپو های public و private را بر روی سیستم شخصی خودتان بک آپ گیری کنید.


پیش نیاز ها
1. پایتون
2. گیت
3. personal access token

این اسکریپت به زبان python کدنویسی شده و باید از قبل روی سیستم python نصب شده باشه ، جهت دانلود از دستور git clone استفاده میکنم که باید گیت رو هم نصب داشته باشید ( که معمولا برنامه نویس ها این 2 ابزار رو نصب دارند از قبل)

جهت دریافت توکن از آموزش زیر استفاده کنید

`https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token
`

بعد از دریافت توکن، مقدار دریافتی را در متغیر github_token ست کنید.

به صورت پیشفرض با اجرای این اسکریپت تمام 300 ریپو public و private شما بر روی مسیری که در متغیر clone_dir ست کردید clone گیری خواهد شد.

`https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-repositories-for-the-authenticated-user
`

جای کار و توسعه بیشتر برای این اسکریپت زیاد هستش ولی من در حد نیاز خودم روش کار کردم ، اگر تمایل داشتید به بهبود این اسکریپت کمک کنید خوشحال میشم برام pull request ارسال کنید.
