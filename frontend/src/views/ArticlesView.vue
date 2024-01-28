<template>
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
    <div class="blog-title">{{ blog.title }}</div>
    <div class="blog-date">{{ blog.created_at.substring(0, 10) }}</div>
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
  display: block;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin-bottom: 10px;
  text-decoration: none;
  color: #333;
  transition:
    background-color 0.3s,
    transform 0.2s;
}

.blog-link:hover {
  background-color: skyblue;
  transform: scale(1.02);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.blog-title {
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
}

.blog-date {
  font-size: 14px;
  color: #888;
}
</style>
