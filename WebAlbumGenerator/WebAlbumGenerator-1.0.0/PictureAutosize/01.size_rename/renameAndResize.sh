#!/bin/bash
imagesDirectory=./images
output=./output
output_s=~/Desktop/PictureAutosize/01.size_rename/output_s
output_b=~/Desktop/PictureAutosize/01.size_rename/output_b

mkdir -p ${output_s}
mkdir -p ${output_b}

i=1
cd ${imagesDirectory}  

for each in *
do
	if [ "$i" -lt 10 ]
	then
		num=00${i}
	elif [ "$i" -lt 100 ]
	then
		num=0${i}
	else
		num=${i}
	fi
		
	echo  ${each} -> photo${num}.JPG;
	mv -f ${each} photo${num}.JPG 
	i=`expr $i + 1`
done

#sipsコマンドの出力先は絶対パスじゃないといけないらしい。

for each in * #そのimagesディレクトリにあるファイルを1個づつ参照する。
 do
 echo ${imagesDirectory}/${each} =\> ${output_b}/${each};
 sips -z 550 800 ${each} --out ${output_b}/${each};
 echo ${imagesDirectory}/${each} =\> ${output_b}/${each};
 sips -z 110 150 ${each} --out ${output_s}/${each};
done
