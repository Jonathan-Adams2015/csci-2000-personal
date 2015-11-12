rm `find . -name *NOTES`
mkdir cleaned_data
cd data
mv `find . -type f` ../cleaned_data/
cd ..
for filename in cleaned_data/*; do mv $filename $filename.txt ; done;

