<template>
  <div class="main-idArticle-edit" v-if="userState.Edit">
    <CreateArticleView
      :blog_id="blogId"
      v-model:title="title"
      v-model:content="content"
      v-model:tag_id="tag_id"
    ></CreateArticleView>
  </div>

  <!-- 显示文章 -->
  <div v-else>
    <div class="showTitle">{{ title }}</div>
    <MdPreview :editorId="id" :modelValue="content" />

    <div class="right-top">
      <MdCatalog
        :editorId="id"
        :scrollElement="scrollElement"
        previewTheme="cyanosis"
      />
    </div>
  </div>
</template>

<script setup>
import { MdPreview, MdCatalog } from 'md-editor-v3'
import 'md-editor-v3/lib/style.css'
// preview.css相比style.css少了编辑器那部分样式
// import 'md-editor-v3/lib/preview.css'

import { ref, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import { useUserStore } from '@/stores/user.js'
import { getBlogIDService } from '@/api/blog.js'
import CreateArticleView from './CreateArticleView.vue'

const userState = useUserStore()
userState.Edit = false // 默认进入IDArticle后清除编辑能力
userState.EditIconDisabled = false // 默认进入IDArticle编辑按钮可用

const route = useRoute()
const id = 'preview-only'
const title = ref('')
const content = ref('')
const tag_id = ref('')

const scrollElement = document.documentElement

const blogId = route.params.id
// const blogTitle = route.params.title
// 使用 async/await 处理异步代码
;(async () => {
  const { data } = await getBlogIDService(blogId)
  content.value = data.content
  title.value = data.title
  tag_id.value = data.tag_id
  console.log('data:', data)
})()

// const blogSave = async () => {
//   const data = await putBlogIDService(blogId, title.value, content.value)
//   if (data.status === 200) {
//     // console.log('blog save success')
//     userState.Edit = false
//     ElMessage({
//       message: 'blog save success',
//       type: 'success'
//     })
//   }
// }

onUnmounted(() => {
  userState.EditIconDisabled = true
})
</script>

<style scoped>
.main-idArticle-edit {
  display: flex;
  flex-direction: column;
  height: 100%;
}
.right-top {
  position: fixed;
  top: 120px;
  right: 4px;
  overflow: auto; /* 使用滚动条来处理超出视口的内容 */
  max-height: 100vh; /* 最大高度不超过视口高度 */
  width: 300px; /* 设置固定宽度，可以根据需要调整 */
  padding: 10px; /* 可以添加一些内边距以确保内容不贴紧边缘 */
  background-color: white; /* 设置背景色，以防内容透明时看不清 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果，提高可读性 */
  z-index: 1000; /* 确保组件在其他元素上方 */
}

.fixed-buttons {
  position: fixed;
  top: 120px;
  left: 100px;
}

.showTitle {
  background-color: #fff;
  color: #000;
  padding: 10px;
  font-size: 36px;
  text-align: center;
  /* 这里可以根据需要添加其他样式 */
}
</style>
