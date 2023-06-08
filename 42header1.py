import os
import datetime
import argparse
import pyautogui

def create_header(file_name, user, email):
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    header = f"""/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   {file_name: <39}            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: {user: <7} {email: <32}   :+:  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: {date_time: <18} by {user: <18}:+:    #+#             */
/*   Updated: {date_time: <18} by {user: <17}###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */"""

    pyautogui.typewrite(header, interval=0.0001)
    pyautogui.hotkey('ctrl', 'v')
    print("Header pasted from script")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_name', required=True, help="The name of the currently open file")
    args = parser.parse_args()

    file_name = args.file_name
    user = "lbaron"
    email = "<lbaron@student.42berlin.de>"
    create_header(file_name, user, email)

