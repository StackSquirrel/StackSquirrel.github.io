echo Deploying RABlog to github

d:
cd D:\Library\Working Documents\gitHub\RAblog\ra

hugo -t hugocards

cd public

git add .

git commit -m "rebuilding site %DATE%"

git push origin master

