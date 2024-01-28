<template>
  <div class="main-create">
    <el-input
      v-model="title"
      style="font-size: 24px; height: 60px"
      placeholder="请输入一个标题"
      clearable
    />
    <MdEditor style="height: 100%" @onSave="blogCreate" v-model="content" />
  </div>
</template>

<script setup>
import { MdEditor } from 'md-editor-v3'
import { postBlogService } from '@/api/blog.js'
// preview.css相比style.css少了编辑器那部分样式
// import 'md-editor-v3/lib/preview.css'
import 'md-editor-v3/lib/style.css'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const router = useRouter()
const content = ref('')
let title = ref('')

const blogCreate = async () => {
  const response = await postBlogService(title.value, content.value)
  // console.log(response)
  if (response.status === 200) {
    // console.log('blog save success')
    const id = response.data.id
    router.push({ path: `/blog/article/${id}` })
    ElMessage({
      message: 'blog create success',
      type: 'success'
    })
  }
}
</script>

<style scoped>
.main-create {
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* 使用组件名作为选择器 类似元素选择器*/
/* 让 MdEditor 占据剩余的全部空间 */
/* MdEditor {
  flex: 1;
} */
</style>
