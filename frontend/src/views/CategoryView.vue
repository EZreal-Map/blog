<template>
  <div class="container-left">
    <el-menu
      :default-active="route.path"
      background-color="efefef"
      :router="true"
    >
      <el-menu-item
        v-for="tag in tags"
        :index="`/blog/categories/${tag}`"
        :key="tag"
      >
        <span>{{ tag }}</span>
      </el-menu-item>
    </el-menu>
  </div>
  <ArticlesView></ArticlesView>
</template>

<script setup>
console.log('CategoryView.vue')
import { ref } from 'vue'
import ArticlesView from '@/views/ArticlesView.vue'
import { useRoute } from 'vue-router'
const tags = ref(['Vue.js', 'JavaScript', 'CSS', 'Python', 'FastAPI', '随想'])

const route = useRoute()
console.log(route.path)
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
