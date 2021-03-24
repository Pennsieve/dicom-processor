# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TEST IMAGE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM pennsieve/base-processor-pandas-test:1-5800e81 as test

RUN apk add --no-cache --update automake \
                                build-base \
                                cmake \
                                curl \
                                gcc \
                                git \
                                pigz \
                                zlib-dev \
                                build-base \
                                autoconf \
                                automake \
                                libtool \
                                zlib-dev \
                                libxml2-dev \
                                jpeg-dev \
                                openjpeg-dev \
                                tiff-dev \
                                glib-dev \
                                gdk-pixbuf-dev \
                                sqlite-dev \
                                libjpeg-turbo-dev \
                                libexif-dev \
                                lcms2-dev \
                                fftw-dev \
                                giflib-dev \
                                libpng-dev \
                                libwebp-dev \
                                orc-dev \
                                poppler-dev \
                                librsvg-dev \
                                libgsf-dev \
                                openexr-dev \
                                gtk-doc \
    && mkdir dcm2niix \
    && git clone https://github.com/rordenlab/dcm2niix.git \
#    && curl -sSL https://github.com/rordenlab/dcm2niix/tarball/v1.0.20171215 | tar xz -C dcm2niix --strip-components 1 \
    && mkdir dcm2niix/build \
    && cd dcm2niix/build \
    && cmake .. && make \
    && make install \
    && rm -rf /tmp/*

COPY dicom_processor/dicom_processor/sanitize.py /app/sanitize.py

WORKDIR /app

ENTRYPOINT [""]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRODUCTION IMAGE
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
FROM pennsieve/base-processor-pandas:1-5800e81 as prod

RUN apk add --no-cache --update automake \
                                build-base \
                                cmake \
                                curl \
                                gcc \
                                git \
                                pigz \
                                zlib-dev \
                                build-base \
                                autoconf \
                                automake \
                                libtool \
                                zlib-dev \
                                libxml2-dev \
                                jpeg-dev \
                                openjpeg-dev \
                                tiff-dev \
                                glib-dev \
                                gdk-pixbuf-dev \
                                sqlite-dev \
                                libjpeg-turbo-dev \
                                libexif-dev \
                                lcms2-dev \
                                fftw-dev \
                                giflib-dev \
                                libpng-dev \
                                libwebp-dev \
                                orc-dev \
                                poppler-dev \
                                librsvg-dev \
                                libgsf-dev \
                                openexr-dev \
                                gtk-doc \
    && mkdir dcm2niix \
    && git clone https://github.com/rordenlab/dcm2niix.git \
#    && curl -sSL https://github.com/rordenlab/dcm2niix/tarball/v1.0.20171215 | tar xz -C dcm2niix --strip-components 1 \
    && mkdir dcm2niix/build \
    && cd dcm2niix/build \
    && cmake .. && make \
    && make install \
    && rm -rf /tmp/*

COPY dicom_processor/dicom_processor/sanitize.py /app/sanitize.py

WORKDIR /app

ENTRYPOINT [""]
