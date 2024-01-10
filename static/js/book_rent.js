//使用 jQuery（在模板中已經引入）或其他方式來處理事件
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function() {
    // 將 CSRF token 添加到所有的 AJAX 請求中
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!settings.crossDomain) {
                const csrftoken = getCookie('csrftoken');
                xhr.setRequestHeader('X-CSRFToken', csrftoken);
            }
        }
    });

    // 以下是你的原始 AJAX 請求
    // ...（你的原始 AJAX 請求代碼）
});


$(document).ready(function() {
    $('.borrow-button').click(function(e) {
        e.preventDefault();
        var bookId = $(this).data('bookid');
        var statusBadge = $('#status-badge-' + bookId);

        $.ajax({
            type: 'POST',
            url: `/borrow/${bookId}/`,
            success: function(response) {
                // 更新狀態
                if (statusBadge.hasClass('bg-success')) {
                    statusBadge.removeClass('bg-success').addClass('bg-danger').text('外借中');
                } else {
                    statusBadge.removeClass('bg-danger').addClass('bg-success').text('可借閱');
                }
            },
            error: function(error) {
                console.error('發生錯誤', error);
            }
        });
    });

    $('.return-button').click(function(e) {
        e.preventDefault();
        var bookId = $(this).data('bookid');
        var statusBadge = $('#status-badge-' + bookId);

        $.ajax({
            type: 'POST',
            url: `/return/${bookId}/`,
            success: function(response) {
                // 更新狀態
                if (statusBadge.hasClass('bg-success')) {
                    statusBadge.removeClass('bg-success').addClass('bg-danger').text('外借中');   
                } else {
                    statusBadge.removeClass('bg-danger').addClass('bg-success').text('可借閱');
                }
            },
            error: function(error) {
                console.error('發生錯誤', error);
            }
        });
    });
});



