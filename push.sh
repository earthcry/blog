#!/bin/bash

# Auto add, commit and push

echo "..."
echo "..."
echo "..."
echo "是否已经git fetch，如否ctr+c"
echo "是否已经git status | git diff | git reflog，如否ctr+c"
echo "是否已经git stash，如否ctr+c"
echo "..."
echo "请按任意键继续"
read -n 1

read -p "请输入提交注释：" note

git add .
git commit -m "$note" # 注释要用引号包括。
git push origin main

#git reflog
