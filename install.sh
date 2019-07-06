pip3 install pyinstaller --user
pyinstaller aptrack.py --clean -F
rm -rf build

dir=$(pwd)
echo "Do you wish to install this program to /usr/bin?"
select yn in "Yes" "No"; do
    case $yn in
        Yes ) sudo cp $dir/dist/aptrack /usr/bin; break;;
        No ) exit;;
    esac
done