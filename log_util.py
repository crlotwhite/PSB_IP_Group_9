def file_log(msg):
    # write msg on file directly
    from datetime import datetime

    with open('log.txt', 'a') as f:
        # formatted datetime like '3 mar 21 => 03/02/2021 21:30:01
        now_str = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        msg = '[{}] {}\n'.format(now_str, msg.replace('\n', ''))
        f.write(msg)