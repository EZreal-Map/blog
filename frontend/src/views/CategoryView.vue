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
  <ArticlesView :tag="route.params.tag"></ArticlesView>
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
  border-right: 1px solid rgb(0 0 0 / 50%);
  padding-top: 5px;
  background-color: #efefef;
}
</style>
