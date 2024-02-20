<template>
  <div class="container-left">
    <el-menu
      :default-active="decodeURIComponent(route.path)"
      background-color="efefef"
      :router="true"
    >
      <!-- decodeURIComponent特定的为url中出现中文解码 -->
      <el-menu-item
        v-for="tag in tags"
        :index="`/blog/categories/${tag.name}`"
        :key="tag.id"
      >
        <span>{{ tag.name }}</span>
      </el-menu-item>
    </el-menu>
  </div>
  <div class="container-main">
    <ArticlesView :tag="route.params.tag"></ArticlesView>
  </div>
</template>

<script setup>
console.log('CategoryView.vue')
import { ref } from 'vue'
import ArticlesView from '@/views/ArticlesView.vue'
import { useRoute } from 'vue-router'
import { getTagListService } from '@/api/tag.js'

const route = useRoute()
console.log('route:', route.path)

const tags = ref()
;(async () => {
  const response = await getTagListService()
  // console.log('response:', response.data)
  tags.value = response.data
})()
</script>

<style scoped>
.container-left {
  position: fixed;
  top: 60px;
  left: 0;
  width: 150px;
  height: 100%;
  border-right: 2px solid rgb(25 25 25 / 20%);
  padding-top: 5px;
  background-color: #f9f9f9;
}

@media (max-width: 1400px) {
  .container-left {
    width: 100px;
  }
  .container-main {
    margin-left: 90px;
  }
}
</style>
