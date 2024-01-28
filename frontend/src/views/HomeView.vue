<template>
  <!-- 最近文章块 -->
  <div class="section">
    <h1>最近文章</h1>
    <ArticlesView></ArticlesView>
  </div>

  <!-- 分类块 -->
  <div class="section">
    <h1>分类</h1>
    <div class="tag-container">
      <div v-for="tag in tags" :key="tag" class="tag">{{ tag }}</div>
    </div>
  </div>

  <!-- GitHub 块 -->
  <div class="section">
    <h1>Github</h1>
    <GithubContribution></GithubContribution>
  </div>
</template>

<script setup>
import GithubContribution from '@/components/GithubContribution.vue'
import ArticlesView from '@/views/ArticlesView.vue'

const tags = ['Vue.js', 'JavaScript', 'CSS', 'Python', 'FastAPI']
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
</style>
