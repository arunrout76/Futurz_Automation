#!/bin/bash

# Set virtual environment
export VIRTUAL_ENV=.\app\Futurz\venv

# Set prompt
if [ -n "$_OLD_VIRTUAL_PROMPT" ]; then
    PROMPT=$_OLD_VIRTUAL_PROMPT
else
    if [ -z "$PROMPT" ]; then
        PROMPT='$P$G'
    fi
    if [ -z "$VIRTUAL_ENV_DISABLE_PROMPT" ]; then
        _OLD_VIRTUAL_PROMPT=$PROMPT
    fi
fi
if [ -z "$VIRTUAL_ENV_DISABLE_PROMPT" ]; then
    if [ -n "" ]; then
        PROMPT="() $PROMPT"
    else
        PROMPT="($(basename "$VIRTUAL_ENV")) $PROMPT"
    fi
fi

# Unset Python home
if [ -n "$_OLD_VIRTUAL_PYTHONHOME" ]; then
    PYTHONHOME=$_OLD_VIRTUAL_PYTHONHOME
fi

# Set PATH
if [ -n "$_OLD_VIRTUAL_PATH" ]; then
    PATH=$_OLD_VIRTUAL_PATH
else
    _OLD_VIRTUAL_PATH=$PATH
fi
PATH=$VIRTUAL_ENV/Scripts:$PATH

# # Run behave with Allure formatter
# behave -f allure_behave.formatter:AllureFormatter -o Report/Allure_Result ./features

# # Generate Allure report
# allure generate Report/Allure_Result -o Report/Allure_Report --clean

# Uncomment the line below if you want to run the send_mail.py script
# python Utility/send_mail.py
