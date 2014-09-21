STRINGS = {
    "en_US": {

        "api": {
            "error_generic": 'Something went wrong!',
            "error_missing_event_handler": 'I don\'t seem to have a handler for the "%s" event.',

        },

        "twilio": {
            "error_generic": '<?xml version="1.0" encoding="UTF-8"?><Response><Sms>Something went wrong! Ow. Try again later.</Sms></Response>',
        },

        "tvrobot": {
            "unrar": """
                     .-=-==--==--.
               ..-=="  ,'o`)      `.
             ,'         `"'         \\
            :  (                     `.__...._
            |                  )    /         `-=-.
            :       ,vv.-._   /    /               `---==-._
             \/\/\/VV ^ d88`;'    /                         `.
                 ``  ^/d88P!'    /             ,              `._
                    ^/    !'   ,.      ,      /                  "-,,__,,--'"'''-.
                   ^/    !'  ,'  \\. .(      (         _           )  ) ) ) ))_,-.\\
                  ^(__ ,!',"'   ;:+.:%:a.     \:.. . ,'          )  )  ) ) ,"'    '
                  ',,,'','     /o:::":%:%a.    \:.:.:         .    )  ) _,'
                   "''       ;':::'' `+%%%a._  \%:%|         ;.). _,-""
                          ,-='_.-'      ``:%::)  )%:|        /:._,"
                         (/(/"           ," ,'_,'%%%:       (_,'
                                        (  (//(`.___;        \\
                                         \\    \\   `         `
              UNRAAAAAAAAAAAAAAAAR        `.    `.   `.        :
                                            \. . .\\   : . . . :
                                             \. . .:    `.. . .:
                                              `..:.:\\    \:...\\
                                               ;:.:.;      ::...:
                                               ):%::       :::::;
                                           __,::%:(        :::::
                                        ,;:%%%%%%%:        ;:%::
                                          ;,--""-.`\\ ,=--':%:%:\\
                                         /"       "| /-".:%%%%%%%\\
                                                         ;,-"'`)%%)   
                                                        /"      "|
                                                            """,

            "unzip": """
                <->      <=>
                 <=>    <->
                  <->  <=>
                   <=><->
                   <-><=>
                    ;--;
                    |  |
                    |  |
                    |LI|    I'MMA UNZIP DIS BITCH
                    \__/
                    <=->
                    <-=>
                    <=->
                    <-=>
                    <=->
                    <-=>
                    <=->
                    <-=>
            """,

            "hello": "Sup everybody. I'm a friendly TvRobot. Beep and whatnot.",

            "kill_caught": "But I was just getting started. Okay fine, I'll stop.",

            "caught_exception": "BEEEEEEEEEEEEEEEEEEEP. OW.",

            "finding_video_file": u"beep booping torrent #%s",
            "moving_video_file": u"beep beep bopping %s file `%s`...",

            "unrecognized_torrent": u"Booeep. Do I know you? Skipping torrent # %s",
            "torrent_downloading": u"Boop. This one is still working. Skipping torrent # %s",
            "unsupported_download_type": u"Beeeeeeeooooppppp I can't do these kinds of downloads yet. :( Skipping torrent # %s",
            "unsupported_schedule_type": u"beepboop %s is an unknown schedule type",
            "unsupported_file_type": u"I don't know how to beep boop this kind of download yet. Skipping torrent # %s",

            "download_clean_completed": "beep. File's done.",

            "adding_torrent": "beep beep. Starting to download this torrent.",
            "adding_magnet": "bzzzzzeeeeep Adding this magnet before it kills me.",
            "adding_duplicate_magnet": "I'm already working on this one, but I'll subscribe you to it since I'm such a nicebot.",
            "adding_download": u"beeboop. Remembering to clean this %s download up later.",
            "add_completed": "Beeped the new torrent."
        }

    }
}

class StringCategory:

    def __init__(self, category_name, string_dict):
        self.category_name = category_name
        self.strings = string_dict

    def __str__(self):
        return "[stringlist:" + self.category_name + "]"

    def __getattr__(self, name):
        return self.strings.get(name, "[" + self.category_name + "." + name + "]")

class Stringifier:

    def __init__(self, lang_id = "en_US"):
        self.lang_id = lang_id
        self.categories = {}

        for category in STRINGS[self.lang_id].keys():
            self.categories[category] = StringCategory(category, STRINGS[self.lang_id][category])

    def __getattr__(self, name):
        return self.categories.get(name, StringCategory(name, {}))