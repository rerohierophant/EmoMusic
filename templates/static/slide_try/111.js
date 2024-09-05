let scrollbar = document.querySelector('.scrollbar');  
let scrollbarContainer = document.querySelector('.scrollbar-container');  
let content = document.querySelector('.content');  
  
let isDragging = false;  
let startY, startScrollTop;  
  
scrollbar.addEventListener('mousedown', function(e) {  
    isDragging = true;  
    startY = e.clientY;  
    startScrollTop = content.scrollTop;  
  
    // 阻止默认事件（如选择文本）  
    e.preventDefault();  
  
    // 监听全局的鼠标移动和鼠标释放事件  
    document.addEventListener('mousemove', onMouseMove);  
    document.addEventListener('mouseup', onMouseUp);  
    document.addEventListener('mouseleave', onMouseUp); // 也处理鼠标离开文档的情况  
});  
  
function onMouseMove(e) {  
    if (!isDragging) return;  
  
    let deltaY = e.clientY - startY;  
    let newScrollTop = startScrollTop - deltaY;  
  
    // 限制滚动位置  
    let maxScrollTop = content.scrollHeight - content.clientHeight;  
    newScrollTop = Math.min(Math.max(0, newScrollTop), maxScrollTop);  
  
    content.scrollTop = newScrollTop;  
  
    // 更新滑动条的位置  
    let scrollPercent = (newScrollTop / maxScrollTop) * 100;  
    scrollbar.style.transform = `translateY(${scrollPercent}%)`;  
}  
  
function onMouseUp() {  
    isDragging = false;  
  
    // 移除事件监听器  
    document.removeEventListener('mousemove', onMouseMove);  
    document.removeEventListener('mouseup', onMouseUp);  
    document.removeEventListener('mouseleave', onMouseUp);  
}  
  
// 还需要处理滚动内容时更新滑动条的位置（之前已经实现）  
content.onscroll = function() {  
    let maxScroll = content.scrollHeight - content.clientHeight;  
    let scrollPercent = (content.scrollTop / maxScroll) * 100;  
    scrollbar.style.transform = `translateY(${scrollPercent}%)`;  
};