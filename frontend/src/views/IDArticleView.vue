<template>
  <MdEditor
    @onSave="blogSave"
    style="height: 88vh"
    v-if="edit"
    v-model="content"
  />
  <div v-else>
    <MdPreview :editorId="id" :modelValue="content" />

    <div class="right-top">
      <MdCatalog
        :editorId="id"
        :scrollElement="scrollElement"
        previewTheme="cyanosis"
      />
    </div>
  </div>
  <div class="fixed-buttons">
    <el-button type="primary" @click="edit = !edit">edit</el-button>
  </div>
</template>

<script setup>
import { MdPreview, MdEditor, MdCatalog } from 'md-editor-v3'
import { getBlogIDService, putBlogIDService } from '@/api/blog.js'
// preview.css相比style.css少了编辑器那部分样式
// import 'md-editor-v3/lib/preview.css'
import 'md-editor-v3/lib/style.css'
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
let edit = ref(false)
const id = 'preview-only'
const content = ref('')
let title = ''
const scrollElement = document.documentElement

const blogId = route.params.id
// const blogTitle = route.params.title
// 使用 async/await 处理异步代码
;(async () => {
  const { data } = await getBlogIDService(blogId)
  content.value = data.content
  title = data.title
})()

const blogSave = async (content) => {
  const data = await putBlogIDService(blogId, title, content)
  if (data.status === 200) {
    // console.log('blog save success')
    edit.value = false
    // eslint-disable-next-line no-undef
    ElMessage({
      message: 'blog save success',
      type: 'success'
    })
  }
}
</script>

<style scoped>
.right-top {
  position: fixed;
  top: 60px;
  right: 0;
  overflow: auto; /* 使用滚动条来处理超出视口的内容 */
  max-height: 100vh; /* 最大高度不超过视口高度 */
  width: 300px; /* 设置固定宽度，可以根据需要调整 */
  padding: 10px; /* 可以添加一些内边距以确保内容不贴紧边缘 */
  background-color: white; /* 设置背景色，以防内容透明时看不清 */
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果，提高可读性 */
  z-index: 1000; /* 确保组件在其他元素上方 */
  word-wrap: break-word; /* 允许在单词内换行 */
  overflow-wrap: break-word; /* 允许在单词内换行（兼容性更好的属性名） */
  white-space: normal; /* 允许文本自动换行 */
}

.fixed-buttons {
  position: fixed;
  top: 120px;
  left: 100px;
}
</style>
