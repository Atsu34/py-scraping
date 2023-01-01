def gui_scraping():
    import Scraping
    import PySimpleGUI as sg
    import time

    scraping = Scraping.scraping()

    layout_first = [[sg.Text("",key="-ACT0-")],
                    [sg.Text('URLを入力'), sg.Input(key='-URL-')],
                    [sg.Text('', key='-ACT1-'),sg.Text("", key="-ACT2-")],
                    [sg.Button("リンク"),sg.Button("画像"),sg.Button("テキスト")],
                    [sg.Button("CSVファイルに保存",key= "-csv-"),sg.Button("ブラウザで開く",key= "-browser-")],
                    [sg.Text("",key="-ACT4-")],
                    [sg.Button('決定'), sg.Button('終了')]]


    window_first = sg.Window('Scraper', layout_first)

    target = ""
    way = ""
    while True:
        event, values = window_first.read()
        if event == sg.WIN_CLOSED or event == '終了':
            break

        if event == 'リンク':
            window_first["-ACT1-"].update(f'リンク')
            target = "links"

        if event == "画像":
            window_first["-ACT1-"].update(f"画像")
            target = "images"

        if event == "テキスト":
            window_first["-ACT1-"].update(f"テキスト")
            target = "texts"

        if event == "-csv-":
            window_first["-ACT2-"].update(f"csvファイルに保存")
            way = "csv"

        if event == "-browser-":
            window_first["-ACT2-"].update(f"ブラウザで開く")
            way = "browser"

        if event == '決定':
            scraping.website_url = values["-URL-"]

            if target == "links":
            
                if way == "csv":
                    try:
                        scraping.links_csv()
                        window_first['-ACT4-'].update(f'成功！')
                    except:
                        window_first["-ACT0-"].update(f"エラーもう一度選択してください。")


                elif way == "browser":
                    try:
                        scraping.links_open()
                        window_first['-ACT4-'].update(f'成功！')
                    except:
                        window_first["-ACT0-"].update(f"エラーもう一度選択してください。")


                elif way == "":
                    window_first["-ACT0-"].update(f"エラーもう一度選択してください。")


            elif target == "":
                window_first["-ACT0-"].update(f"エラーもう一度選択してください。")



            if target == "images":
                if way == "csv":
                    try:
                        scraping.imgs_csv()
                        window_first['-ACT4-'].update(f'成功！')
                    except:
                        window_first["-ACT0-"].update(f"エラーもう一度選択してください。")

                elif way == "browser":
                    try:
                        scraping.imgs_open()
                        window_first['-ACT4-'].update(f'成功！')
                    except:
                        window_first["-ACT0-"].update(f"エラーもう一度選択してください。")

                elif way == "":
                    window_first["-ACT0-"].update(f"エラーもう一度選択してください。")


            elif target == "":
                window_first["-ACT0-"].update(f"エラーもう一度選択してください。")



            if target == "texts":
                if way == "csv":
                    try:
                        scraping.texts_csv()
                        window_first['-ACT4-'].update(f'成功！')
                    except:
                        window_first["-ACT0-"].update(f"エラーもう一度選択してください。")
                elif way == "browser":
                    window_first["-ACT0-"].update(f"テキストはブラウザで開けません。")



                elif way == "":
                    window_first["-ACT0-"].update(f"エラーもう一度選択してください。")


            elif target == "":
                window_first["-ACT0-"].update(f"エラーもう一度選択してください。")


    window_first.close()