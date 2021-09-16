"
 Software Name : botenv
 SPDX-FileCopyrightText: Copyright (c) 2021 Orange
 SPDX-License-Identifier: GPL-2.0-only

 This software is distributed under the GNU General Public License v2 only,
 the text of which is available at https://spdx.org/licenses/GPL-2.0-only.html
 or see the 'LICENCE' file for more details.

 Author: Elkin AGUAS <elkin.aguas@orange.com>
"

if [ "$#" -gt 0 ]
then
    if [ "$0" == "r1" ] || [ "$1" == "r1" ] || [ "$2" == "r1" ] || [ "$3" == "r1" ] || [ "$4" == "r1" ]
    then
        ( xterm -e "vagrant halt r1" )
    fi &

    if [ "$0" == "to11" ] || [ "$1" == "to11" ] || [ "$2" == "to11" ] || [ "$3" == "to11" ] || [ "$4" == "to11" ]
    then
        ( xterm -e "vagrant halt to11" )
    fi &

    if [ "$0" == "to12" ] || [ "$1" == "to12" ] || [ "$2" == "to12" ] || [ "$3" == "to12" ] || [ "$4" == "to12" ]
    then
        ( xterm -e "vagrant halt to12" )
    fi &

    if [ "$0" == "to13" ] || [ "$1" == "to13" ] || [ "$2" == "to13" ] || [ "$3" == "to13" ] || [ "$4" == "to13" ]
    then
        ( xterm -e "vagrant halt to13" )
    fi &

    if [ "$0" == "to14" ] || [ "$1" == "to14" ] || [ "$2" == "to14" ] || [ "$3" == "to14" ] || [ "$4" == "to14" ]
    then
        ( xterm -e "vagrant halt to14" )
    fi &

    if [ "$0" == "to15" ] || [ "$1" == "to15" ] || [ "$2" == "to15" ] || [ "$3" == "to15" ] || [ "$4" == "to15" ]
    then
        ( xterm -e "vagrant halt to15" )
    fi &

    if [ "$0" == "to16" ] || [ "$1" == "to16" ] || [ "$2" == "to16" ] || [ "$3" == "to16" ] || [ "$4" == "to16" ]
    then
        ( xterm -e "vagrant halt to16" )
    fi &

    if [ "$0" == "to17" ] || [ "$1" == "to17" ] || [ "$2" == "to17" ] || [ "$3" == "to17" ] || [ "$4" == "to17" ]
    then
        ( xterm -e "vagrant halt to17" )
    fi &

    if [ "$0" == "ub" ] || [ "$1" == "ub" ] || [ "$2" == "ub" ] || [ "$3" == "ub" ] || [ "$4" == "ub" ]
    then
        ( xterm -e "vagrant halt ub" )
    fi &

    if [ "$0" == "cc" ] || [ "$1" == "cc" ] || [ "$2" == "cc" ] || [ "$3" == "cc" ] || [ "$4" == "cc" ]
    then
        ( xterm -e "vagrant halt cc" )
    fi &

    if [ "$0" == "loader" ] || [ "$1" == "loader" ] || [ "$2" == "loader" ] || [ "$3" == "loader" ] || [ "$4" == "loader" ]
    then
        ( xterm -e "vagrant halt loader" )
    fi
else
    ( xterm -e "vagrant halt r1" ) &
    ( xterm -e "vagrant halt to11" ) &
    ( xterm -e "vagrant halt to12" ) &
    ( xterm -e "vagrant halt to13" ) &
    ( xterm -e "vagrant halt to14" ) &
    ( xterm -e "vagrant halt to15" ) &
    ( xterm -e "vagrant halt to16" ) &
    ( xterm -e "vagrant halt to17" ) &
    ( xterm -e "vagrant halt ub" ) &
    ( xterm -e "vagrant halt cc" ) &
    ( xterm -e "vagrant halt loader" )
fi