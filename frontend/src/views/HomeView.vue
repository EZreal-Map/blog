<template>
  <!-- 最近文章块 -->
  <div class="section">
    <h1>最近文章</h1>
    <ArticlesView :limit="computeLimit" :maxLimit="maxLimit"></ArticlesView>
  </div>

  <!-- 分类块 -->
  <div class="section">
    <h1>分类</h1>
    <div class="tag-container">
      <div v-for="tag in tags" :key="tag" class="tag">
        <router-link :to="{ name: 'tag-category', params: { tag: tag.name } }">
          {{ tag.name }}
        </router-link>
      </div>
    </div>
  </div>

  <!-- GitHub 块 -->
  <div class="section">
    <h1>Github</h1>
    <GithubContribution></GithubContribution>
    <!--<img src="https://ghchart.rshah.org/EZreal-Map" alt="Name Your Github chart">-->
  </div>
</template>

<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import GithubContribution from '@/components/GithubContribution.vue'
import ArticlesView from '@/views/ArticlesView.vue'
import { getTagListService } from '@/api/tag.js'

const tags = ref()
;(async () => {
  const response = await getTagListService()
  console.log('response:', response)
  tags.value = response.data
})()

const minLimit = 1
const maxLimit = 5

const screenHeight = ref(window.innerHeight - 500)

// 监听窗口大小变化
const handleResize = () => {
  screenHeight.value = window.innerHeight - 500
}

// 在组件挂载时添加窗口大小变化的监听
onMounted(() => {
  window.addEventListener('resize', handleResize)
})

// 在组件销毁时移除窗口大小变化的监听
onUnmounted(() => {
  window.removeEventListener('resize', handleResize)
})

// 使用computed返回新的计算结果
const computeLimit = computed(() => {
  let limit = Math.floor(screenHeight.value / 90)
  // 添加限制条件
  if (limit < minLimit) {
    limit = minLimit
  } else if (limit > maxLimit) {
    limit = maxLimit
  }
  return limit
})
</script>

<style scoped>
.section {
  margin-bottom: 20px;
}

.section h1 {
  font-size: 24px;
  color: #fff; /* Set the text color to white */
  background-color: #297fb8; /* Set the background color */
  padding: 10px; /* Add padding for better visual */
  border-radius: 5px; /* Add border-radius for rounded corners */
  box-shadow: 0 8px 8px rgba(0, 0, 0, 0.1); /* Add a box shadow */
  transition:
    background-color 0.3s,
    box-shadow 0.3s; /* Add transitions for smooth hover effect */
}
.tag-container {
  display: flex;
  flex-wrap: wrap; /* 在空间不足时自动换行 */
  gap: 12px;
  margin-top: 20px;
}

.tag {
  background-color: #eee;
  /* color: #fff; */
  padding: 10px 15px;
  border-radius: 25px;
  font-size: 16px;
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
}

.tag:hover {
  background-color: skyblue;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}

.tag a {
  text-decoration: none; /* 禁用下划线 */
  color: inherit; /* 继承父元素的文字颜色 */
  /* 可以根据需要添加其他样式 */
}
</style>
