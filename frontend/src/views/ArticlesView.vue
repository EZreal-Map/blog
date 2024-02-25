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
import { onMounted, shallowRef, watch } from 'vue'
import { RouterLink } from 'vue-router'
import { getBlogListService } from '@/api/blog.js'

const props = defineProps({
  limit: {
    type: Number,
    default: null
  },
  tag: {
    type: String,
    default: null
  },
  maxLimit: {
    type: Number,
    default: null
  }
})
const blogs = shallowRef([])
let maxBlogs

onMounted(async () => {
  // 其他页面不因为界面高度伸缩变化而动态调整 limit，此时props.limit永远为null，全部获取
  if (props.maxLimit === null) {
    const response = await getBlogListService(props.limit, props.tag)
    blogs.value = response.data
  } else {
    // maxLimit有值的时候，来自于 HomeView.vue 首页，进行伸缩变化调整 limit
    const response = await getBlogListService(props.maxLimit, props.tag)
    maxBlogs = response.data
    blogs.value = maxBlogs.slice(0, props.limit)
  }
})

// 子组件时刻监听tag变化，才能触发子组件页面更新，与开启IDArticleView.vue不同之处
watch(
  () => props.tag,
  async (tag) => {
    const data = await getBlogListService(props.limit, tag)
    blogs.value = data.data
  }
)

watch(
  () => props.limit,
  async (limit) => {
    if (maxBlogs) {
      blogs.value = maxBlogs.slice(0, limit)
    }
  }
)
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
