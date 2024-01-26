<template>
  <div class="main">Articles</div>
  <!-- 跳转并携带params参数（to的对象写法） -->
  <RouterLink
    v-for="blog in blogs"
    :key="blog.id"
    :to="{
      name: 'id-article', //用name跳转
      params: {
        id: blog.id
      }
    }"
    class="blog-link"
  >
    {{ blog.title }} - {{ blog.created_at }}
  </RouterLink>
</template>
<script setup>
console.log('Articles.vue')
import { onMounted, shallowRef } from 'vue'
import { RouterLink } from 'vue-router'

import { getBlogListService } from '@/api/blog.js'

const blogs = shallowRef([])
onMounted(async () => {
  const data = await getBlogListService()
  // console.log(data)
  blogs.value = data.data
  // text.value = data.content
})
</script>
<style scoped>
.blog-link {
  display: block; /* 让每个链接以块级元素显示 */
  margin-bottom: 10px; /* 设置下边距，使它们在垂直方向上分隔开 */
  text-decoration: none; /* 去掉链接的下划线 */
  color: #333; /* 设置链接文本颜色 */
  background-color: skyblue;
}
</style>
